using System.Collections.Generic;
using Microsoft.AspNetCore.Identity;

namespace Server.Areas.Identity.Data
{
    public enum Conditions
    {
        HeartDisease,
        Diabetes,
        AutonomicDisease,
        Addiction
    }
    
    public class CorvinaUser : IdentityUser
    {
        [PersonalData]
        public string Condition;
    }
}