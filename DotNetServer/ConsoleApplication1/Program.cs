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
            var s = new UdpSocket();
            s.Start("192.168.50.85", 50000, "test", verbose: true);

            // Thread.Sleep(1000);
            // s.SendTo("192.168.50.1", 50056, Message.CreateConnectionMessage("test", hashPass: true).ToJson());
            Thread.Sleep(1000);
            s.SendTo("192.168.50.1", 50056, Message.CreateOldConnectionMessage("test", 50000, hashPass: true).ToJson());
            Thread.Sleep(1000);
            s.SendTo("192.168.50.1", 50056, new Message(7, "{}").ToJson());
            Thread.Sleep(1000);
            // s.SendTo("192.168.50.1", 50056, Message.CreateOldCommandsMessage().ToJson());
            // Thread.Sleep(1000);

            // Console.WriteLine(new OldConnectionMessage("test", 50000, true).ToJson());
            // var cmd = new OldRobotData().ToJson();
        }
    }
}

// {"id": 2, "parity": 1, "len": 24, "message": "{\"answer\" : \"CONNECTED\"}"}

/*
{"id": 8, "parity": 1, "len": 1124, "message": "{\"targets\": {\"rAnkleRX\": {\"position\": 0, \"torque\": 0}, \"lAnkleRX\": {\"position\
": 0, \"torque\": 0}, \"rAnkleRZ\": {\"position\": 0, \"torque\": 0}, \"lAnkleRZ\": {\"position\": 0, \"torque\": 0}, \"rShoulderRY\": {\
"position\": 0, \"torque\": 0}, \"lShoulderBaseRY\": {\"position\": 0, \"torque\": 0}, \"rShoulderBaseRY\": {\"position\": 0, \"torque\":
 0}, \"lShoulderRY\": {\"position\": 0, \"torque\": 0}, \"rShoulderRZ\": {\"position\": 0, \"torque\": 0}, \"lShoulderRZ\": {\"position\"
: 0, \"torque\": 0}, \"rKneeRX\": {\"position\": 0, \"torque\": 0}, \"lKneeRX\": {\"position\": 0, \"torque\": 0}, \"rHipRX\": {\"positio
n\": 0, \"torque\": 0}, \"lHipRX\": {\"position\": 0, \"torque\": 0}, \"rHipRY\": {\"position\": 0, \"torque\": 0}, \"lHipRY\": {\"positi
on\": 0, \"torque\": 0}, \"rHipRZ\": {\"position\": 0, \"torque\": 0}, \"lHipRZ\": {\"position\": 0, \"torque\": 0}, \"headRX\": {\"posit
ion\": 0, \"torque\": 0}, \"rElbowRX\": {\"position\": 0, \"torque\": 0}, \"lElbowRX\": {\"position\": 0, \"torque\": 0}, \"torsoRY\": {\
"position\": 0, \"torque\": 0}}, \"imu_datas\": {\"accelerationX\": 0, \"accelerationY\": 0, \"accelerationZ\": 0, \"rotationX\": 0, \"ro
tationY\": 0, \"rotationZ\": 0, \"MagnX\": 0, \"MagnY\": 0, \"MagnZ\": 0}, \"lidar_datas\": []}"}

*/