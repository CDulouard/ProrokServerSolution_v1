﻿using System;
using System.Net;
using System.Threading;


namespace ConsoleApplication1
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var s = new UdpSocket();
            s.Start("127.0.0.1", 27000, "test");

            s.SendTo("127.0.0.1", 27000, "pilou");
            Thread.Sleep(1000);
            s.CreatConnection(new IPEndPoint(IPAddress.Parse("127.0.0.1"), 27000));
            Thread.Sleep(1000);
            s.Send("text");
            Thread.Sleep(1000);

            Console.ReadKey();
            
        }
    }
}