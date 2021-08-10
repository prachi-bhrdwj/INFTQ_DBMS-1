#exercise3
CREATE TABLE match(
Mid INTEGER ,
Tid INTEGER CONSTRAINT match_tid references TOURNAMNET(Tid),
player1 INTEGER CONSTRAINT mtch_ply1 references player(Pid),
player2 INTEGER CONSTRAINT mtch_ply2 references player(Pid),
MatchDt DATE NOT NULL,
Winner INTEGER CONSTRAINT mtch_win references player(Pid),
Score VARCHAR2(30) NOT NULL,
CONSTRAINT mtch_mid_pk PRIMARY KEY(Mid,Tid),
CONSTRAINT mtch_ply_ck CHECK(player1 <> player2)

);

#exercise4
ALTER TABLE player ADD(Matchesplayed NUMBER,Matcheswon NUMBER);

#exercise7
ALTER TABLE player DROP(ContactNo);

#exercise8
ALTER TABLE player RENAME COLUMN PId to PlayerId;

#exercise9
ALTER TABLE player MODIFY Pname VARCHAR2(50);

#exercise
#exercise
#exercise
#exercise
#exercise
#exercise

#assignment5
CREATE TABLE store(
Name VARCHAR2(20) PRIMARY KEY,
Location VARCHAR2(30)NOT NULL,
ManagerName VARCHAR2(30) UNIQUE
);

#assignment6
ALTER TABLE store RENAME COLUMN Name to StoreName;

#assignment7
CREATE TABLE bill(
BillNo NUMBER PRIMARY KEY,
StoreName VARCHAR2(20) REFERENCES store(StoreName),
ShopperId NUMBER REFERENCES shopper(ShopperId),
Arcode CHAR(5) REFERENCES article(Arcode),
amount NUMBER,
BillDate DATE ,
Quantity NUMBER(4) DEFAULT 1 CHECK(Quantity >0));


#assignment8
CREATE TABLE supplier(
SupplierId VARCHAR2(6) PRIMARY KEY,
Name VARCHAR2(30) ,
ContactNo VARCHAR2(15) NOT NULL,
EmailId VARCHAR2(30)
);

#assignment9
ALTER TABLE supplier ADD City VARCHAR2(10);

#assignment10
ALTER TABLE supplier DROP COLUMN EmailId;
