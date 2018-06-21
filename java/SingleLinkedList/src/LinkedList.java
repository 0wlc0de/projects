public class LinkedList {

    private Node first;

    public LinkedList() {
        first = null;
    }

    public void add(String val) {
        insert(val);
    }

    public void add(int pos, String val) {
        insert(pos, val);
    }

    private void insert(String val) {
        final Node node = new Node(val);
        node.setNext(first);

        first = node;
    }

    private void insert(int pos, String val) {
        Node node = first;
        final Node newNode = new Node(val);
        if(pos <= 1){
            insert(val);
            return;
        }
        for(int x = 1; x<pos-1; x++) {
            if(node.getNext() == null) break;
            else node = node.getNext();
        }

        newNode.setNext(node.getNext());
        node.setNext(newNode);
    }

    public void delete(String val) {
        Node node = first;
        Node prev = null;
        while(node != null) {
            if(val.equals(node.getValue())) {
                prev.setNext(node.getNext());
                break;
            }
            prev = node;
            node = node.getNext();
        }
        System.gc();
    }

    public void printList() {
        getAllElements(this.first);
    }

    private void getAllElements(final Node node) {

        if(node == null) return;
        System.out.println("(" + node.getIndex() + ", " + node.getValue() + ") ");
        getAllElements(node.getNext());
    }


    public String search(String val) {
        Node node = first;
        while(node != null) {
            if(val.equals(node.getValue()))
                return "The node is in the list";
            else
                node = node.getNext();
        }

        return "cannot find the node in the list.";
    }






}
