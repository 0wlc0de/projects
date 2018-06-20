public class main {
    public static void main(String[] args) {
        LinkedList linkedList = new LinkedList();
        linkedList.add(10);
        linkedList.add(0);
        linkedList.add(11);
        linkedList.add(11);
        linkedList.add(12);

        linkedList.print();
        System.out.println("\nSize of list : " + linkedList.getSize());

    }
}
