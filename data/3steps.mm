<map version="0.9.0">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1403194070953" ID="ID_1284794540" LINK="blogging.mm" MODIFIED="1403194156356">
<richcontent TYPE="NODE"><html>
  <head>
    
  </head>
  <body>
    <p style="text-align: center">
      3 Simple steps
    </p>
    <p style="text-align: center">
      to test your new
    </p>
    <p style="text-align: center">
      Arduino Clone
    </p>
  </body>
</html></richcontent>
<node CREATED="1403194937689" ID="ID_374151022" MODIFIED="1403621370654" POSITION="right" TEXT="Is your brainchild going to work?">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      You've built your latest (or maybe your first) Arduino clone. It might be breaboarded, or on stripboard, or a PCB. You've visually checked the connections, over and over, and maybe done some quick continuity checks with a multimeter. Everything looks fine. But will it actually work?
    </p>
    <p>
      
    </p>
    <p>
      Follow these three steps to check it out.
    </p>
  </body>
</html>
</richcontent>
</node>
<node CREATED="1403619167044" ID="ID_830303203" MODIFIED="1403621383169" POSITION="right" TEXT="blink- The Secret Sauce">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Here's my secret sauce forbuilding clones:
    </p>
    <ol>
      <li>
        Use a chip that has both a bootloader and th standard blink sketch pre-loaded.
      </li>
      <li>
        Use a 5V LED for testing.
      </li>
    </ol>
    <p>
      Let's look at those in a bit more detail.
    </p>
  </body>
</html></richcontent>
<node CREATED="1403619606684" ID="ID_1861619798" MODIFIED="1403619694019" TEXT="Use a chip that has both a bootloader and th standard blink sketch pre-loaded">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      When you test your clone with a pre-prepared chip, you're starting with a known good core component. If the blighter
    </p>
    <p>
      doesn't blink you know you've made a mistake in the wiring.
    </p>
  </body>
</html></richcontent>
</node>
<node CREATED="1403195756090" ID="ID_812019919" MODIFIED="1403619829380" TEXT="A 5v LED is the tester&apos;s friend">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      Many makers have yet to discover the wonders of the 5V LED. In case thes components are new to you, I'll explain what they are and why they work so well in this situation.
    </p>
    <p>
      
    </p>
    <p>
      Normally you need to use LEDs in series with an appopriate load resistor.&#160;This limits the current through the LED. If you omit the load resistor, the LED will rapidly burn out.
    </p>
    <p>
      
    </p>
    <p>
      With 5V LEDs, you don't need an external load resistor because the LED maker has built one into the LED. You can connect the LED across 5V directly and it will light up, confirming that there's 5V between ti (negative) cathode and (postiive) anode. You can tell which is which because the anode is the longer lead, just like a normal LED.
    </p>
    <p>
      
    </p>
    <p>
      I love 5V LEDs and use them a lot. Plug one into your circuit across your power supply rails, and you have an instant power-on indicator. Connect the anode to +5V and the cathode to pin 13 (whcih is adjacent) and the blink sketch will flash your LED on or off. Place one across ground and TXD or RXD and you can see if serial data is being transmited.
    </p>
    <p>
      
    </p>
    <p>
      Share this with your friends: A 5v LED is the tester's friend.
    </p>
    <p>
      
    </p>
    <p>
      If you're in the UK you can get the ones I use from Farnell. Farnell also stock 3.3V LEDs which are useful if you're working with a Raspberry Pi, an mbed or a teesny 3.x.
    </p>
    <p>
      
    </p>
    <p>
      If the LED doesn't come on when you connect things, disconnect quickly and move on to troubleshooting.
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1403195161714" ID="ID_591822992" MODIFIED="1403620221048" POSITION="right" TEXT="Next, load a sketch">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      I'm going to make a couple of assumptions here: your Arduino clone has some way of uploading a sketch, and it involves an FTDI cable or equivalent. Since 95% of the clones I've seen satisfy this criterion, it's pretty likely that this applies to you.
    </p>
    <p>
      
    </p>
    <p>
      In that case, the next step is simple. Connect your clone to your computer, and try to upload a sketch.
    </p>
    <p>
      
    </p>
    <p>
      There are a couple of things to watch out for here; you'll need to make sure that the Arduino IDE has the right board and the right port selected.
    </p>
    <p>
      
    </p>
    <p>
      I develop on Linux, and the FTDI cable normally shows up as /dev/ttyacm0. If you're not sure how to find out whcih port to use, the Arduino website has good advice for Windows, Linux and OS/X users.
    </p>
    <p>
      
    </p>
    <p>
      You'll also need to tell the Arduino IDE what board you're programming. If you're using an Atmel ATMega328p (which I recommend) with a 16 MHz crystal (which I also recommend), chose <font face="FreeMono"><i>Arduino Duemilanove w/ Atmega328</i></font>
    </p>
  </body>
</html></richcontent>
<node CREATED="1403195673945" ID="ID_1491005358" MODIFIED="1403620429368" TEXT="Which sketch should you use?">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      The simplest sketch to use is the Basics/Blink example. Open it from the Arduino IDE and click the upload Icon. The IDE will show you when it's compiled and will then upload it.
    </p>
    <p>
      
    </p>
    <p>
      You're looking for a message '<i>done uploading</i>' on the status bar. If you see that, the upload worked; go on the next step. If not, go to troubleshooting.
    </p>
    <p>
      
    </p>
  </body>
</html></richcontent>
</node>
</node>
<node CREATED="1403195846186" ID="ID_467323043" MODIFIED="1403621502190" POSITION="right" TEXT="Now tweak it and marvel at your success">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      If you are as skeptical as a good engineer should be, you'll want to do one more test: change the blink sketch and watch your clone's behaviour change.
    </p>
    <p>
      
    </p>
    <p>
      Edit the sketch by changing the delays in the LED blinking loop from 1000 to 100. After the change, the relevant bit of the sketch should look something like this:
    </p>
    <p>
      
    </p>
    <p>
      <font face="Courier 10 Pitch">// the loop routine runs over and over again forever: </font>
    </p>
    <p>
      <font face="Courier 10 Pitch">void loop() { </font>
    </p>
    <p>
      <font face="Courier 10 Pitch">&#160;&#160;digitalWrite(led, HIGH);&#160;&#160;&#160;// turn the LED on (HIGH is the voltage level) </font>
    </p>
    <p>
      <font face="Courier 10 Pitch">&#160;&#160;delay(<b>100</b>);&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;// don't wait for a second :)</font>
    </p>
    <p>
      <font face="Courier 10 Pitch">&#160;&#160;digitalWrite(led, LOW);&#160;&#160;&#160;&#160;// turn the LED off by making the voltage LOW </font>
    </p>
    <p>
      <font face="Courier 10 Pitch">&#160;&#160;delay(<b>100</b>);&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;// wait for a tenth of a second </font>
    </p>
    <p>
      <font face="Courier 10 Pitch">}</font>
    </p>
    <p>
      
    </p>
    <p>
      When you have uploaded the changed sketch you should see the LED blinking much faster. If so, you're done. You have a working clone. Time for a break and a celebration!
    </p>
  </body>
</html>
</richcontent>
</node>
<node CREATED="1403197354141" ID="ID_1257960846" LINK="Troublshooting.mm" MODIFIED="1403620774625" POSITION="right" TEXT="Troublshooting">
<richcontent TYPE="NOTE"><html>
  <head>
    
  </head>
  <body>
    <p>
      We'll look at troublshooting in another post.
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
</map>
