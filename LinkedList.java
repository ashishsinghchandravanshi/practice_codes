import java.util.Scanner;

public class LinkedList {
    private Node head;

    public class Node {
        Object data;
        Node next;

         Node(Object data) {
            this.data = data;
            this.next = null;
        }
    }

    
    public void addFirst(Object data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            newNode.next = head;
            head = newNode;
        }
    }
    public void addLast(Object data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current=head;
            while(current.next!=null){
                current=current.next;
            }
            current.next=newNode;
        }
    }

    public void deleteFirst(Object data) {
    if(head==null){
        System.out.println("empty");
    }else{
        head.next=head;
    }
}
    public void deleteLast(Object data) {
        if(head==null){
            System.out.println("empty");
        }else{
              Node Secondlast=head;
              Node last=head.next;
              while(lastNode.next!=null){
                lastNode=lastNode.next;
                secondlast=secondLast.next;
              }
              secondlast.next=null;


    }
}
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList list = new LinkedList();
        
        System.out.print("Enter a number: ");
        
        int a= sc.nextInt();  
        sc.nextLine();
        list.addFirst(a); 
       
        System.out.print("Enter a number: ");
        String b= sc.nextLine();  
        
        list.addFirst(b);  
       

     System.out.print("Enter a number: ");
        String c= sc.nextLine();  
        
        list.addLast(c); 

        list.printList();
    }
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }
}
