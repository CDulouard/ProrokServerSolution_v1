using System.Collections.Generic;
using Newtonsoft.Json;

namespace ConsoleApplication1
{
    public class RobotDataMessage
    {
        public Dictionary<string, int> servomotors_position;
        public Dictionary<string, int> cc_motosr_speed;

        [JsonConstructor]
        public RobotDataMessage(Dictionary<string, int> servomotorsPosition, Dictionary<string, int> CCMotors)
        {
            servomotors_position = servomotorsPosition;
            cc_motosr_speed = CCMotors;
        }
        
        public RobotDataMessage(string jsonString)
        {
            try
            {
                var jsonObj = JsonConvert.DeserializeObject<RobotDataMessage>(jsonString);
                servomotors_position = jsonObj.servomotors_position;
                cc_motosr_speed = jsonObj.cc_motosr_speed;
            }
            catch (JsonReaderException e)
            {
                servomotors_position = new Dictionary<string, int>();
                cc_motosr_speed = new Dictionary<string, int>();
            }
        }

        public string ToJson()
        {
            return JsonConvert.SerializeObject(this);
        }
    }
}