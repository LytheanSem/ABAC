//Lythean Sem
//6511925

package u6511925;

public class Driver {
    public static void main(String[] args) {
        Worklist<Integer> iQueue = new Queue<Integer>();
        iQueue.add(4);
        iQueue.add(7);
        iQueue.add(11);


        Worklist<String> sQueue = new Queue<String>();
        sQueue.add("Happy");
        sQueue.add("Chinese");
        sQueue.add("New Year");

        System.out.println("Integer Queue:");
        while (iQueue.hasMore()) {
            System.out.println(iQueue.remove());
        }

    }
}
