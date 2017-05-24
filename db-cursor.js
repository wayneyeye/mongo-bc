var cursor=db.test.find();
while(cursor.hasNext()){
	obj=cursor.next();
	print(obj.baz);
}

var cursor=db.test.find().sort({baz:-1}).skip(295).limit(300);
while(cursor.hasNext()){
	obj=cursor.next();
	print(obj.baz);
}