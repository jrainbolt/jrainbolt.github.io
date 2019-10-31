public class Bacon extends BurgerDecorator {
    //Cost of an add-on is $2.00
    private double cost = 2.00;

    //Super inherits data member from parent abstract class BurgerDecorator
    public Bacon(Burger specialBurger){
        super(specialBurger);
    }
    //makeBurger is called which calls the method from the parent class, and then adds the cost of the add() function
    public double makeBurger(){
        return specialBurger.makeBurger() + addBacon();
    }
    //the add() function adds the add-on, and returns the cost which is 2.00. Also prints to System.out the add-on name.
    private double addBacon(){
        System.out.println(" + Bacon $2.00");
        return cost;
    }
}
