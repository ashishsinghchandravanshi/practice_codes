import java.util.Scanner;
public class calculation{
    public static void main(String[] args){
                    Scanner sc=new Scanner(System.in);
        int result;
        while(true){
        System.out.println("enter first number");
        int a=sc.nextInt();
        System.out.println("enter second number");
        int b=sc.nextInt();
        
        System.out.println("press 1 for Addition");
        System.out.println("press 2 for Subtraction");
        System.out.println("press 3 for Multiplication");
        System.out.println("press 4 for Division");
        System.out.println("press 5 for exit");
        
        System.out.println("chhose operator");
        int choose=sc.nextInt();
        if(choose==1){
            result=a+b;
            System.out.println("result");
            System.out.println(result); 
        }
       else if(choose==2){
                result=a-b;
                System.out.println("result");
                System.out.println(result); 
       }
        else if(choose==3){
                    result=a*b;
                    System.out.println("result");
                    System.out.println(result);   
        }          
        else if(choose==4){
                        result=a/b;
                        System.out.println("result");
                        System.out.println(result); 
        }
        else if(choose==5){
              break; 
        }
        else {
        System.out.print("invalid");      
    }
        System.out.println("press 0 for exit otherwise press 1 for continue");
        int choice=sc.nextInt();
        if(choice==0){
            break;
        }
    }

    }
}
