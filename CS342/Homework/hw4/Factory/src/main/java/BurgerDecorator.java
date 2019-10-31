abstract class BurgerDecorator implements Burger{
    //abstract class used to create an instance of the Burger interface.
    protected Burger specialBurger;

    //Constructor used to create an instance of a Burger object.
    public BurgerDecorator(Burger specialBurger){
        this.specialBurger = specialBurger;
    }
}
