//Lythean Sem
//6511925

package u6511925;

public class Queue<T> implements Worklist<T> {
    private Node<T> front = null;
    private Node<T> rear = null;

    @Override
    public void add(T item) {
        Node<T> newNode = new Node<>(item, null);
        if (rear == null) {
            front = rear = newNode;
            return;
        }
        rear.next = newNode;
        rear = newNode;
    }

    @Override
    public boolean hasMore() {
        return front != null;
    }

    @Override
    public T remove() {
        if (front == null) {
            return null;
        }
        T data = front.getData();
        front = front.getNext();
        if (front == null) {
            rear = null;
        }
        return data;
    }
}
