public class BasicBurger implements Burger {

    //Cost of a basic burger
    private double cost = 6.50;
    //Override modifies the makeBurger() method from the Burger interface.
    @Override
    public double makeBurger(){
        System.out.println("Basic Cheeseburger $6.50");
        return cost;
    }
}
