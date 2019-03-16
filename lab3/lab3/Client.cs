using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab3
{
    [Table("client")]
    public class Client
    {
        [Column("id")]
        public int ClientId { get; set; }
        public string FIO { get; set; }
        public string email { get; set; }
    }
}
