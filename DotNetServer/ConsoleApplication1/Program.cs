using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net;
using System.Security.Cryptography;
using System.Threading;


namespace ConsoleApplication1
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var s = new UdpSocket();
            // s.Start("127.0.0.1", 50000, "test", verbose:true);
            // s.Start("127.0.0.1", 27000, "test", verbose:true);
            
            // s.SendTo("127.0.0.1", 50000, "ping");
            // Thread.Sleep(1000);
            //
            // var msgToSend = Message.CreateConnectionMessage("test", hashPass:true);
            // s.SendTo("127.0.0.1", 50000, new Message(101, msgToSend).ToJson());
            // Thread.Sleep(1000);
            
            // msgToSend = Message.CreateConnectionMessage("testi", hashPass:true);
            // s.SendTo("127.0.0.1", 50000, new Message(101, msgToSend).ToJson());
            // Thread.Sleep(1000);
            
            // s.SendTo("192.168.43.81", 50000, "retest");
            // Thread.Sleep(1000);
            // s.SendTo("128.0.0.1", 27000, "tst");
            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.2", 27000, "tst");
            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.1", 27000, "retest");
            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.1", 27000, "retest");
            
            // s.CreatConnection(new IPEndPoint(IPAddress.Parse("127.0.0.1"), 27000));
            // Thread.Sleep(1000);
            // s.Send("text");
            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.1", 27000, "pilou");

            // Console.WriteLine(s.Ping("127.0.0.1", 50000));

            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.1", 50000, "top");
            

            // Console.ReadKey();

            var servoDico = new Dictionary<string, int>();
            servoDico["motor1"] = 50;
            servoDico["motor2"] = 100;
            servoDico["motor3"] = 150;
            var ccDico = new Dictionary<string, int>();
            ccDico["motor1"] = 50;
            ccDico["motor2"] = 100;
            ccDico["motor3"] = 150;
            var test = new RobotDataMessage(servoDico, ccDico);
            Console.WriteLine(test.ToJson());
            
            
            Console.WriteLine(new RobotDataMessage(test.ToJson()).ToJson());

        }
    }
}