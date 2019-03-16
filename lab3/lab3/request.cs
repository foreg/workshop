using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Web;

namespace lab3
{
    [Table("request")]
    public class Request
    {
        [Column("id")]
        public int RequestId { get; set; }
        public DateTime date { get; set; }

        [Column("client_id")]
        public int ClientId { get; set; }

        [Column("service_id")]
        public int ServiceId { get; set; }
    }
}