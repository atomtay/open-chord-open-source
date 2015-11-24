var express = require('express');
var app = express();

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true}));

app.use(express.static('static_files'));

var sqlite3 = require("sqlite3").verbose();
var db = new sqlite3.Database('accounts.db');


//Create
app.post('/users', function (req, res) {
	var postBody = req.body;
	var myName = postBody.name;
	if(!myName) {
		//res.send("boys love toys");
		return;
	}
	//res.send("boys love toys2");
	db.each('select name from people', function(err, row) {
		//res.send("boys love toys3");
		if(row.name.toString() == myName)
		{
			//res.send('ERROR');
			return;
		}
		
	});
	var prep = db.prepare("insert into people values (?,?,?,?,?,?)");
	prep.run(postBody.name, postBody.user, postBody.pass, '','','');
	prep.finalize();	
	res.send("OK");
});

//READ
app.get('/users/*', function (req, res) {
	var nameToLookup = req.params[0];

	db.all("select * from people where username='" + nameToLookup + "'", function(err, row) {
		res.send(row[0]);
		return;
	});
	//res.send("{}");
});


//login
app.post('/users/login/*', function (req, res) {
	var nameToLookup = req.params[0];
	
	db.each("select password from people where username='" + nameToLookup + "'", function(err, row) {
		if (row.password == req.body.pass) {
			res.send("OK");
		}
		else{
			res.send("NO");
		}
	});
});

//read all users
app.get('/all', function(req, res) {
	console.log("k");
	db.all("select username from people", function(err, row) {
		console.log("p");
		res.send(row);
	});
});

//update
app.post('/users/update/*', function(req,res) {
	var nameToLookup = req.params[0];
	var postBody = req.body;

	db.run("update people set name='" + postBody.name +"',location='" + postBody.location + "',instruments='" + postBody.instruments + "',bio='" + postBody.bio + "' where username='" + postBody.user + "'");
	res.send("OK");
});

var server = app.listen(3000, function() {
	var port = server.address().port;
	console.log('Server started at http://localhost:%s/', port);
	});