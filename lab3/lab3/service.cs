using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace lab3
{
    [Table("service")]
    public class Service
    {
        [Column("id")]
        public int ServiceId { get; set; }
        public string name { get; set; }
        public double price { get; set; }
    }
}