import java.util.*;

class Adder extends Thread{
    private ArrayList<Integer> arr;
    private int start,end;
    public static int sum;


    public Adder(ArrayList<Integer> a,int s,int e){
        this.start = s;
        this.arr = a;
        this.end = e;
        this.start();
    } 

    @Override
    public void run(){
        synchronized(this.arr){
            for(int i=start;i<end;i++){
                sum+=arr.get(i);
            }
        }

    }
}

public class threads{

    public static void main(String[] agrs){
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=0;i<100;i++){
            arr.add(i,1);
        }

        Adder a = new Adder(arr,0,25);
        a.sum = 0;
        Adder b = new Adder(arr, 25, 50);
        Adder c = new Adder(arr, 50, 75);
        Adder d = new Adder(arr, 75, 100);

        try{
            a.join();
            d.join();
            b.join();
            c.join();
        }catch(Exception e){
            e.printStackTrace();
        }

        System.out.println("Final sum: "+a.sum);
        

    }

}