using System;
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
            s.Start("192.168.50.85", 50001, "test", verbose:true);
            // s.Start("127.0.0.1", 27000, "test", verbose:true);
            
            s.SendTo("192.168.50.85", 50000, "retest");
            Thread.Sleep(1000);
            // s.SendTo("128.0.0.1", 27000, "tst");
            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.2", 27000, "tst");
            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.1", 27000, "retest");
            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.1", 27000, "retest");
            var msgToSend = new Message(5, "");
            // s.CreatConnection(new IPEndPoint(IPAddress.Parse("127.0.0.1"), 27000));
            // Thread.Sleep(1000);
            // s.Send("text");
            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.1", 27000, "pilou");

            // Thread.Sleep(1000);
            // s.SendTo("127.0.0.1", 50000, "pilou");
            

            Console.ReadKey();

        }
    }
}