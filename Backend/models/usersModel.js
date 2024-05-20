// const db=require('../util/database')

// model.exports = class{
 
// construtor(username , email,password){
//     this.username=username,
//     this.email=email;
//     this.password=password;
// }

//   save(){
//     return db.execute('insert into users (username , email,password) values (?,?,?)',[this.username,this.email,this.password])
// }


// };


const db = require('../util/database');

const User = {
  create: async (Name, Email, Password) => {
    const [result] = await db.execute(
      'INSERT INTO users (Name, Email, Password) VALUES (?, ?, ?)',
      [Name, Email, Password]
    );
    return result;
  },
  
  findByEmail: async (email) => {
    const [rows] = await db.execute('SELECT * FROM users WHERE Email = ?', [email]);
    return rows[0];
  },
  
  findById: async (id) => {
    const [rows] = await db.execute('SELECT * FROM users WHERE id = ?', [id]);
    return rows[0];
  }
};

module.exports = User;


