void idsLedUP(){ //Function to connect a server to send information as WI
  WiFiClient client = server.available(); //Check if a client's connected
  if (!client) {
    delay(10); 
    return;
  }
  while (client.connected()) {
    if (client.available()) {
      String request = client.readStringUntil('\n'); //Get 1,0 or -1 
      Serial.print(request);
      if(request=="0"){//IDS traffic it's OK
        ok++; //Add counter to ok traffic
        digitalWrite(LED_1,HIGH);
        delay(1000);
        digitalWrite(LED_1,LOW);
      }
      else if (request=="1"){//IDS traffic, it's warning
        warningMessage = true;dangerMessage=false;
        senderMessageLog(warningMessage,dangerMessage); //Send logs to Telegram
        digitalWrite(LED_2,HIGH);
        delay(1000);
        digitalWrite(LED_2,LOW);
        warning++;//Add counter to warning traffic
      }else if(request=="-1"){ //IDS traffic, it's danger
        warningMessage = false;dangerMessage=true;
        senderMessageLog(warningMessage,dangerMessage); //Sends DANGER alert
        digitalWrite(LED_3,HIGH);
        delay(1000);
        digitalWrite(LED_3,LOW);
        danger++;//Add counter to danger traffic
        emailSender++; //Number of times that it's sent a message
        digitalWrite(Bzzer, HIGH);   // turn on the buzzer 
        delay(1000);                 // wait
        digitalWrite(Bzzer , LOW);  // turn off the buzzer
      }
      client.stop();
      telegramBotService();
      //pingTargets();//Generate traffic
    }
  }
}


//Ping tags

void pingTargets(){
  bool google = Ping.ping("www.google.com",pingNumber);
  bool tbs = Ping.ping("www.tbs.co.jp",pingNumber);
  bool github = Ping.ping("github.com",pingNumber);
  bool mywebsite = Ping.ping("yoshiokeimakun.me",pingNumber);
  if(!google ||!tbs|| !github || !mywebsite){
    digitalWrite(LED_4,LOW);
    return;
  }else{
    digitalWrite(LED_4,HIGH);
  }
  delay(10);
}
//Telegram Bots
//Options functions for Telegram bot
void logsMessages(String option){
  if(option == "/start"){ //Function Start
    String startMessage = "Hi, @"+(String)msg.sender.username+"\nThis bot alerts you about your traffic in your ESP32\nPlease, use command /options .";
    myBot.sendMessage(msg.sender.id,startMessage);
  }else if(option = "/options"){ //Function Options
    String opString  = "/options\t\t To show options\n/logs\t\t Show you  all number of logs\n/email\t\t Show you if any email has been sent.";
    myBot.sendMessage(msg.sender.id,opString);
  }
}
//Get number of logs
void logsCounter(){
  String logMessage = "You have number of logs by category:\nOk: "+(String)ok+"\nWarning: "+(String)warning+"\nDanger: "+(String)danger;
  myBot.sendMessage(msg.sender.id, logMessage);
  return;
}
//Get if an email has sent
void numberSendEmail(){
  String logEmail = "An email has sent "+(String)emailSender+" number of times";
  myBot.sendMessage(msg.sender.id, logEmail);
  return;
}
//Sends notifications to elegram
void senderMessageLog(bool warningMessage, bool dangerMessage){
  if((warningMessage==true) && (dangerMessage == false)){
     String messageStatus = "WARNING! A suspicious packet was detected on your network";
     myBot.sendMessage(msg.sender.id, messageStatus);
  }else if ((warningMessage==false) && (dangerMessage == true)){
     String messageStatus = "DANGER! A issue packet was detected on your network";
     myBot.sendMessage(msg.sender.id, messageStatus);
    }else if  ((warningMessage==false) && (dangerMessage == false)){
      String messageStatus = "A package was lost while the IDS was working";
      myBot.sendMessage(msg.sender.id, messageStatus);
    }
}

//Telegram bot main

void telegramBotService(){
  if(myBot.getNewMessage(msg)){
    if(msg.messageType == CTBotMessageText){
      if(msg.text.equalsIgnoreCase("/start")){ //Start case
        logsMessages(msg.text);
      }else if (msg.text.equalsIgnoreCase("/options")){ //Options case
        logsMessages(msg.text);
      }else if (msg.text.equalsIgnoreCase("/logs")){ //Logs case
        logsCounter();
      }else if (msg.text.equalsIgnoreCase("/email")){//Email case
        numberSendEmail();
      }else{
        myBot.sendMessage(msg.sender.id, msg.text);//Error message
        myBot.sendMessage(msg.sender.id, "UPS! Try with: /options");
      }
    }
  }
}
