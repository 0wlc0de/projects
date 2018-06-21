public class main {
    private static final LinkedList list = new LinkedList();

    public static void main(String[] args) {
        list.add("String 1");
        list.add("String 2");
        list.add("String 3");
        list.add(5, "test 2222");

        list.printList();
        System.out.println();
        list.add(4, "test 1111");
        list.printList();
        System.out.println();
        list.delete("String 1");
        list.printList();
    }
}
