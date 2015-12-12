var express = require('express');
var app = express();
var router= express.Router();
var multer = require("multer");
var path = require("path");
var fs = require("fs");
var img = "";
var gm = require("gm");

//taken from Stack overflow, multer set up for uploads
var options = multer.diskStorage({ destination: 'static_files/uploads/' ,
	filename: function (req,file,cb) {
		cb(null, img = (Math.random().toString(36)+'00000000000000000').slice(2, 10) + Date.now() + path.extname(file.originalname));
	}
});
var upload = multer({ storage: options });

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true}));

app.use(express.static('static_files'));

var sqlite3 = require("sqlite3").verbose();
var db = new sqlite3.Database('accounts.db');

//db.run("create table pics(username varchar(100), image varchar(500))")
//db.run("create table people(name varchar(100), username varchar(100) primary key, password varchar(100), location varchar(100), instruments varchar(100), bio varchar(500))");


//homepage
app.get('/',function(req,res){
	res.sendFile(__dirname + "index.html");
});

//Create
/*
app.post('/create/', function (err, req, res, next) {
	var postBody = req.body;
	var myName = postBody.user;
	if(!myName) {
		console.log("yes");
		return;
	}
	console.log("madeit!");
	db.run("create table " + postBody.user + "solo(track varchar(500), name varchar(100))");
	db.run("create table " + postBody.user + "remix(track varchar(500), name varchar(100))");
	var prep = db.prepare("insert into people values (?,?,?,?,?,?)");
	prep.run(postBody.name, postBody.user, postBody.pass, '','','');
	prep.finalize();	
	var otherprep = db.prepare("insert into pics values (?,?)");
	otherprep.run(postBody.user, "");
	otherprep.finalize();
	res.send("OK");
	
});
*/
app.post('/users', function (err, req, res) {
	var postBody = req.body;
	var myName = postBody.user;
	
	

	db.run("create table " + postBody.user + "solo(track varchar(500), name varchar(100))");
	db.run("create table " + postBody.user + "remix(track varchar(500), name varchar(100))");

	var prep = db.prepare("insert into people values (?,?,?,?,?,?)");
	prep.run(postBody.name, postBody.user, postBody.pass, '','','');
	prep.finalize();	

	var otherprep = db.prepare("insert into pics values (?,?)");
	otherprep.run(postBody.user, "");
	otherprep.finalize();
	res.send("OK");
	
});

//POST photo upload
app.post("/uploads/images/*", upload.single('file'), function(req,res) {
	var thisUser = req.params[0];

	var prep = db.prepare("update pics set image=? where username=?");
	prep.run("/uploads/" +img,thisUser);
	prep.finalize();
	//res.sendFile(__dirnae + "/static_files/index.html");
	res.send("OK");
});


//POST solo upload
app.post("/uploads/solos/*", upload.single('file'), function(req,res) {
	var thisUser = req.params[0];

	//db.run("create table if not exists '" + thisUser + "solo'(track varchar(500))");

	var prep = db.prepare("insert into " + thisUser + "solo values (?,?)");
	prep.run("/uploads/" + img, req.file.originalname);
	prep.finalize();
	res.send("OK");
});

//POST remix upload
app.post("/uploads/remixes/*", upload.single('file'), function(req,res){
	var thisUser = req.params[0];

	var prep = db.prepare("insert into " + thisUser + "remix values (?,?)");
	prep.run("/uploads/" + img, req.file.originalname);
	prep.finalize();
	res.send('OK');
});

//READ profile
app.get('/users/*', function (req, res) {
	var nameToLookup = req.params[0];

	db.all("select * from people where username='" + nameToLookup + "'", function(err, row) {
		res.send(row[0]);
		return;
	});
	//res.send("{}");
});

//READ profile pic
app.get('/uploads/images/*', function(req, res) {
	var nameToLookup = req.params[0];

	db.all("select * from pics where username='" + nameToLookup + "'", function(err, row) {
		res.send(row[0]);
		return;
	});
});

//READ solo tracks
app.get("/uploads/solos/*", function(req,res){
	var nameToLookup = req.params[0];
	var filepairs = {

	};
	var count = 0;
	db.all("select * from "+ nameToLookup + "solo", function(err, row){
		res.send(row);
	});
});

//READ remixes
app.get("/uploads/remixes/*", function(req, res){
	var nameToLookup = req.params[0];

	db.all("select * from " + nameToLookup + "remix", function(err, row){
		res.send(row);
	});
});

/*
//READ
app.get("/downloads/*", function(req,res){
	var track = req.params[0];
	var file = __dirname + track;
	res.download(file, function(){});
});
*/

//READ instruments
app.get("/instruments", function(req,res){
	db.all("select instruments from people", function(err, row){
		res.send(row);
	});
});

app.get("/instruments/*", function(req,res){
	db.all("select username from people where instruments='" + req.params[0] + "'", function(err,row){
		//console.log(row);
		res.send(row);
	});
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
	db.all("select username from people", function(err, row) {
		res.send(row);
	});
});

//update
app.put('/users/*', function(req,res) {
	var nameToLookup = req.params[0];
	var postBody = req.body;

	db.run("update people set name='" + postBody.name +"',location='" + postBody.location + "',instruments='" + postBody.instruments + "',bio='" + postBody.bio + "' where username='" + postBody.user + "'");
	res.send("OK");
});

//delete
app.delete("/users/*", function(req,res) {
	var nametoDelete = req.params[0];

	db.run("delete from people where username='" + nametoDelete +"'");
	db.run("delete from pics where username='" + nametoDelete + "'");
	res.send("OK");
});

var server = app.listen(3000, function() {
	var port = server.address().port;
	console.log('Server started at http://localhost:%s/', port);
	});