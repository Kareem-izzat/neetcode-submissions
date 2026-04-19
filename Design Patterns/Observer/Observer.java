import java.util.ArrayList;
import java.util.List;


interface Observer {
    void update();
}


interface Subject {
    void registerObserver(Observer o);
    void removeObserver(Observer o);
    void notifyObservers();
}


class WeatherStation implements Subject {

    private final List<Observer> observers = new ArrayList<>();

    private float temperature;
    private float humidity;

    public void setMeasurements(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;

        notifyObservers();
    }


    public float getTemperature() {
        return temperature;
    }

    public float getHumidity() {
        return humidity;
    }

    @Override
    public void registerObserver(Observer o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    @Override
    public void notifyObservers() {
        for (Observer o : observers) {
            o.update();
        }
    }
}


class PhoneDisplay implements Observer {

    private final WeatherStation weatherStation;

    public PhoneDisplay(WeatherStation ws) {
        this.weatherStation = ws;
    }

    @Override
    public void update() {
        System.out.println(" Phone Display");
        System.out.println("Temperature: " + weatherStation.getTemperature());
        System.out.println("Humidity: " + weatherStation.getHumidity());
        System.out.println("----------------------");
    }
}


class TVDisplay implements Observer {

    private final WeatherStation weatherStation;

    public TVDisplay(WeatherStation ws) {
        this.weatherStation = ws;
    }

    @Override
    public void update() {
        System.out.println("📺 TV Display");
        System.out.println(
                "Temp = " + weatherStation.getTemperature() +
                        " | Humidity = " + weatherStation.getHumidity()
        );
        System.out.println("======================");
    }
}


class Main4 {
    public static void main(String[] args) {

        WeatherStation weatherStation = new WeatherStation();

        Observer phone = new PhoneDisplay(weatherStation);
        Observer tv = new TVDisplay(weatherStation);

        weatherStation.registerObserver(phone);
        weatherStation.registerObserver(tv);

        // First update
        weatherStation.setMeasurements(25f, 60f);

        // Second update
        weatherStation.setMeasurements(30f, 70f);
    }
}