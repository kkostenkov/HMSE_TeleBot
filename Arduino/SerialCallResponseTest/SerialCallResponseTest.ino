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

// ________________ Pins ________________________
const int DOOR_SENSOR_PIN  = 3;
// ________________________________________________

// ________________ Timers ________________________
unsigned long lastTempCheckTime;
int tempCheckDelay = 30000; // 30 sec
unsigned long lastDoorCheckTime;
int doorCheckDelay = 1000; // 1 sec
unsigned long lastFullReportTime;
int fullReportDelay = 30000; // 30 sec

// ________________________________________________

// ________________ Sensor values ________________
float temperature;
bool doorIsClosed;
bool doorWasClosed;
// _______________________________________________

// Command codes
const String C_STATUS = "s";
const String T_STATUS = "t";
const String R_STATUS = "r";

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
  doorWasClosed = true;
  refreshDoorStatusData();
  lastDoorCheckTime = millis();
  makeFullReport();
  lastFullReportTime = millis();
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
  // temp
  if (lastTempCheckTime + tempCheckDelay < now)
  {
    refreshTemperatureData();
    lastTempCheckTime = now;
  }
  // door
  if (lastDoorCheckTime + doorCheckDelay < now)
  {
    refreshDoorStatusData();
    lastDoorCheckTime = now;
  }

  // full report
  if (lastFullReportTime + fullReportDelay < now)
  {
    //makeFullReport(); // Not sending explicitly before python code supports.
    lastFullReportTime = now;
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
  else if (command == T_STATUS)
  {
    Serial.println(temperature);
  }
  else if (command == R_STATUS)
  {
    makeFullReport();
  }
  else 
  {
    Serial.println("Default response to " + command);
  }
}

//  ________________ FULL REPORT____________________
void makeFullReport()
{
  String report = "{ \"temp\" : " + String(temperature) + ", \"doorClosed\" : " + String(doorIsClosed) +" }";
  Serial.println(report); 
}
//  ________________________________________________

//  ________________ TEMP____________________
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

// _________________DOOR__________________
void refreshDoorStatusData()
{
  //int doorSensorValue = digitalRead(DOOR_SENSOR_PIN);
  doorIsClosed = digitalRead(DOOR_SENSOR_PIN) > 0.5f;
  if (doorIsClosed != doorWasClosed)
    {    
      Serial.println("{ \"doorClosed\" : " + String(doorIsClosed) + " }");
      doorWasClosed = doorIsClosed;
    }
}

