public class LinkedList {
    private Node first, last;
    private int size;

    public void add(Integer value) {
        insert(value);
    }

    private void insert(Integer value) {
        final Node node = new Node(value);
        if(first == null)
            first = node;
        else {
            last.setNext(node);
        }
        size+=1;
        last = node;
    }

    public void print() {
        getAllElements(first);
    }

    private void getAllElements(Node node) {
        if(node == null)
            return;
        System.out.print(node.getValue() + " ");
        getAllElements(node.getNext());
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
}
