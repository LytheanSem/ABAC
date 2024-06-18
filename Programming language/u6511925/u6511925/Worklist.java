//Lythean Sem
//6511925

package u6511925;

public interface Worklist<T>  {
    void add(T item);
    boolean hasMore();
    T remove();
}
