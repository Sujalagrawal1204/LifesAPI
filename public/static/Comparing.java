import java.util.Comparator;
import java.util.*;

class StudentComparator implements Comparator<Student>{
    @Override
    public int compare(Student s,Student s2){
        return Integer.compare(s.roll, s2.roll);
    }
}
class Student implements Comparable<Student>{
    String name;int age,roll;
    public Student(String n,int r,int a){
        this.name = n;
        roll = r; age = a;
    }

    public void getDetails(){
        System.out.println("Student Details");
        System.out.println("Name: "+this.name);
        System.out.println("Age: "+this.age);
        System.out.println("Roll Number: "+this.roll);
    }

    @Override
    public int compareTo(Student s){
        return Integer.compare(this.roll,s.roll);
    }
}

public class Comparing {

    public static void main(String args[]){
        List<Student> list = new ArrayList<>();
        list.add(new Student("Saurabh", 60, 20));
        list.add(new Student("Rashmi", 11, 19));
        list.add(new Student("Shreyansh", 61, 20));

        // System.out.println("Using Comparator: ");
        // Collections.sort(list,new StudentComparator());
        System.out.println("Using Comparable: ");
        Collections.sort(list);

        Iterator itr = list.iterator();

        int j = 0;
        System.out.println("Using Iterator: ");
        while(itr.hasNext()){
            Student s = (Student)itr.next();
            System.out.println((++j)+" "+s.name);
        }

        System.out.println("Using Normal For Loop: ");
        for(int i=0;i<list.size();i++){
            Student s = list.get(i);
            System.out.println((i+1)+" "+s.name);
        }

    }
    
}
