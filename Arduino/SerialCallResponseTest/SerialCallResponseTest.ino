#include <OneWire.h>
#include <DallasTemperature.h>


// __________________OneWire Setup_________________
// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 2
// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);
// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);
// arrays to hold device address
DeviceAddress insideThermometer;
// ________________________________________________

// ________________ Timers ________________________
unsigned long lastTempCheckTime;
int tempCheckDelay = 60000; // 60 sec
// ________________________________________________

// ________________ Sensor values ________________
float temperature;
// _______________________________________________

// Command codes
const String C_STATUS = "s";
const String T_STATUS = "t";

void setup()
{
  Serial.begin(9600);
  
  // _______ OneWire ________
  // locate devices on the bus
  Serial.print("Locating devices...");
  sensors.begin();
  Serial.print("Found ");
  Serial.print(sensors.getDeviceCount(), DEC);
  Serial.println(" devices.");
  // report parasite power requirements
  Serial.print("Parasite power is: "); 
  if (sensors.isParasitePowerMode()) Serial.println("ON");
  else Serial.println("OFF");
  // search for devices on the bus and assign based on an index.  
  if (!sensors.getAddress(insideThermometer, 0)) Serial.println("Unable to find address for Device 0");   
  // set the resolution to 9 bit (Each Dallas/Maxim device is capable of several different resolutions)
  sensors.setResolution(insideThermometer, 9);
  // _________________ Prepare inital sensor data _______
  refreshTemperatureData();
  lastTempCheckTime = millis();
  //

}

void loop()
{
  // _______ Serial ______
  if (Serial.available())
  {
     parseCommand(Serial.readString());
  }

  // ______ Timers ______
  unsigned long now = millis();
  if (lastTempCheckTime + tempCheckDelay < now)
  {
    refreshTemperatureData();
    lastTempCheckTime = now;
    Serial.println(temperature);
  }

  // ______ Sleep _______
  
  delay(100);
  
}

void parseCommand(String command)
{
  if (command == C_STATUS)
  {
    Serial.println("Status report: OK");
  }
  else if (command = T_STATUS)
  {
    Serial.println(temperature);
  }
  else 
  {
    Serial.println("Default response to " + command);
  }
}

void refreshTemperatureData()
{
  temperature = requestTemperature(insideThermometer);
}

float requestTemperature(DeviceAddress deviceAddress)
{
  sensors.requestTemperatures(); // Send the command to get temperatures
  float tempC = sensors.getTempC(deviceAddress);
  return tempC;
}


