int bluePin = 11;
int greenPin = 10;
int redPin = 9;

char color;
int r = 0;
int g = 0;
int b = 0;
char num = 0;

char *p, *i;
int x;

void setup(){
  pinMode(bluePin,OUTPUT);
  pinMode(greenPin,OUTPUT);
  pinMode(redPin,OUTPUT);
  Serial.begin(9600);
}

void setColor(int red, int green, int blue){
  
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}

char* subStr (char* input_string, char *separator, int segment_number) {
 char *act, *sub, *ptr;
 static char copy[20];
 int i;
 
 strcpy(copy, input_string);
 
for (i = 1, act = copy; i <= segment_number; i++, act = NULL) {
 
 sub = strtok_r(act, separator, &ptr);
 if (sub == NULL) break;
 }
 return sub;
}

void loop(){ 

  char buffer[] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
  
  while (!Serial.available());
  Serial.readBytesUntil('\n', buffer, 11);
  
  for (int x=1; x<=3;x++){
    switch (x){
      case 1:
         r = atoi(subStr(buffer,",",x));
      case 2:
         g = atoi(subStr(buffer,",",x));
      case 3:
         b =atoi(subStr(buffer,",",x));
    }  
  }
  
  Serial.println(r);
  Serial.println(g);
  Serial.println(b);
  
  setColor(r,g,b);
}
