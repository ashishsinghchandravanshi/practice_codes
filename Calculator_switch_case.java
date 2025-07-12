import java.util.Scanner;
public class Calculator{
    public static void calculator(String[] args){
        
        Scanner sc = new Scanner(System.in);
        int result;
        while(true){
        System.out.println("enter first number");
        int a= sc.nextInt();
        System.out.println("enter second number");
        int b= sc.nextInt();
        
        System.out.println("choose 1-add,2-subtract,3-multiply,4-division,5-exit");
        int operator=sc.nextInt();
        switch(operator){
            case 1:
        result=a+b;
        System.out.println("Result");
           System.out.println(result);
           break;
           case 2:
           System.out.println("Result");
         result=a-b;
           System.out.println(result);
           break;
           case 3:
          result=a*b;
          System.out.println("Result");
           System.out.println(result);
           break;
           case 4:
           result=a/b;
           System.out.println("Result");
           System.out.println(result);
           break;
           case 5:
           break;
           default:
           System.out.println("invalid option");

        }
        System.out.println("for exit  enter 0 for continue enter 1");
        int chooseoption=sc.nextInt();
        if(chooseoption==0){
            break;

        }
    }  
    }
        
    }
