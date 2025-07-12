import java.util.Scanner;
public class loop{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int i,sum=1;
        for(i=1; i<=5; i++){
            sum=sum*i;
            System.out.println(sum);
        }
    }
}