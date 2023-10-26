package hello;

public class hello {

    public static void main(String[] args) 
    {

        if (args.length > 0)
        {
            System.out.println("Testsvar: "+args[0]);

        } 
        else 
        {
    
            System.out.println("One argument expected.\n");
        }
    }
}