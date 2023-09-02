import java.io.*;
import java.util.*;

public class Files {
    public static void reader(String path){
        File f = new File(path);
            if(f.isDirectory()){
                File list[] = f.listFiles();
                for(File file :list){
                    if(file.isDirectory()){
                        reader(file.getAbsolutePath());
                    }else if(file.isFile()){
                        System.out.println(file.getName());
                    }
                }
            }else{
                System.out.println(f.getName());
            }
    }
    public static void main(String args[]){
        reader(".");
    }
}
