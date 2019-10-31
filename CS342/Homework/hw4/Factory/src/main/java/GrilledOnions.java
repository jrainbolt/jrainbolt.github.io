public class GrilledOnions extends BurgerDecorator {
    //Cost of an add-on is $2.00
    private double cost = 2.00;

    //Super inherits data member from parent abstract class BurgerDecorator
    public GrilledOnions(Burger specialBurger){
        super(specialBurger);
    }
    //makeBurger is called which calls the method from the parent class, and then adds the cost of the add() function
    public double makeBurger(){
        return specialBurger.makeBurger() + addGrilledOnions();
    }
    //the add() function adds the add-on, and returns the cost which is 2.00. Also prints to System.out the add-on name.
    private double addGrilledOnions(){
        System.out.println(" + Grilled Onions $2.00");
        return cost;
    }
}
