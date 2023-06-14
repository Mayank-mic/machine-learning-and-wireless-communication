int data;

void setup() 
{ 
  Serial.begin(9600); 
  pinMode(10, OUTPUT); 
  digitalWrite (10, LOW); //initially set to low
  Serial.println("This is my First Example.");
}
 
void loop() 
{
if (Serial.available()>0)
  {
    data = Serial.read();
  

  if (data == '1')
  digitalWrite (10, HIGH);

  else if (data == '0')
  digitalWrite (10, LOW);
  }
}