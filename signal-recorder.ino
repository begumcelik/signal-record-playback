
int inputs[8];
int prev_inputs[8];

unsigned long time_stamp;
unsigned long last_change_time[8];
int debounce_time = 1;

bool change;

int pin_no1 = 34;
int pin_no2 = 35;
int pin_no3 = 36;
int pin_no4 = 37;
int pin_no5 = 38;
int pin_no6 = 39;
int pin_no7 = 40;
int pin_no8 = 41;

void setup() {
  // Start serial connection
  Serial.begin(28800);

  // Define the input pins as pull-up resistors
  pinMode(pin_no1, INPUT_PULLUP);
  pinMode(pin_no2, INPUT_PULLUP);
  pinMode(pin_no3, INPUT_PULLUP);
  pinMode(pin_no4, INPUT_PULLUP);
  pinMode(pin_no5, INPUT_PULLUP);
  pinMode(pin_no6, INPUT_PULLUP);
  pinMode(pin_no7, INPUT_PULLUP);
  pinMode(pin_no8, INPUT_PULLUP);

  for (int i = 0; i < 8; i++)
  {
    last_change_time[i] = 0;
  }
}

void loop() {

  change = false;

  time_stamp = millis();

  inputs[0] = digitalRead(pin_no1); // input1
  inputs[1] = digitalRead(pin_no2); // input2
  inputs[2] = digitalRead(pin_no3); // input3
  inputs[3] = digitalRead(pin_no4); // input4
  inputs[4] = digitalRead(pin_no5);  // input5
  inputs[5] = digitalRead(pin_no6);  // input6
  inputs[6] = digitalRead(pin_no7);  // input7
  inputs[7] = digitalRead(pin_no8);  // input8


  for (int i = 0; i < 8; i++)
  {
    if (inputs[i] != prev_inputs[i] && time_stamp > last_change_time[i] + debounce_time)
    {
      change = true;
      last_change_time[i] = time_stamp;
    }
  }

  if (change)
  {
    for (int i = 0; i < 8; i++)
    {
      Serial.print(inputs[i]);
    }
    Serial.print(";"); 
    Serial.print(time_stamp);
    Serial.print("*");
  }  

  for (int i = 0; i < 8; i++)
  {
    prev_inputs[i] = inputs[i];
  }

}
