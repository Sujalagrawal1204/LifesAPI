import java.io.*;
import java.util.*;

class Student implements Serializable{
    String name;int age,roll;
    public Student(String n,int r,int a){
        this.name = n; this.age = a; this.roll = r;
    }
    public void getDetails(){
        System.out.println("Student Details");
        System.out.println("Name: "+this.name);
        System.out.println("Age: "+this.age);
        System.out.println("Roll Number: "+this.roll);
        System.out.println();
    }
}

public class Handling{
 public static void main(String args[]){

    try(FileOutputStream ofs = new FileOutputStream("./file.txt")){
        ObjectOutputStream oos = new ObjectOutputStream(ofs);
        oos.writeObject(new Student("Sauabh", 60, 20));
        oos.writeObject(new Student("Rashmi", 11, 19));
        oos.writeObject(new Student("Shreyansh", 61, 20));

    }catch(Exception e){
        e.printStackTrace();
    }



    try(FileInputStream fis = new FileInputStream("./file.txt")){
        ObjectInputStream ois = new ObjectInputStream(fis);
        while(true){
            try{
                Student s = (Student)ois.readObject();
                s.getDetails();
            }catch(EOFException e){
                break;
            }catch(Exception e){
                e.printStackTrace();
            }            
        }
    }catch(Exception e){
        e.printStackTrace();
    }

 
    
 }   
}