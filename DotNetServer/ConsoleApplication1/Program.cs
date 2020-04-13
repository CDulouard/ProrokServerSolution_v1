using System;
using System.Collections.Generic;
using Newtonsoft.Json;
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
            var sIp = "128.0.0.1";
            var sPort = 50000;
            var s = new UdpSocket();
            Console.WriteLine(s.IsActive);
            s.Start(sIp, sPort, "test", verbose: true);
            Thread.Sleep(1000);
            s.SendTo(sIp, sPort, "ping");
            Thread.Sleep(1000);


            // for (int i = 0; i < 3; i++)
            // {
            //     s.SendTo("192.168.43.81", 50000,
            //         Message.CreateOldConnectionMessage("test", 50000, hashPass: true).ToJson());
            //     Thread.Sleep(1000);
            // }
        }
    }
}