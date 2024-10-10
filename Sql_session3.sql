/*
Data Types:
String Data Type:
	Char --> fixed length strig stores upto 255 characters (n bytes, where n is the length)
    Varchar --> Variable length string, stores upto 65535 (1byte + length of the string)
    Enum(v1,v2,v3..) --> allows to set a list of possible values to a column (col_name ENUM(val1,val2..) constraint)
    SET(v1,v2,..) --> allows to specify a column where each value can be a set of zero or more values chosen from a predifined list of possible values.(upto 64 values)
    Text() --> holds string with length upto 65,535 bytes

Numeric Data Types:
	TINYINT() --> Signed range -128 to 127, unsigned range 0 to 255
    SMALLINT() --> Signed range -32768 to 32767, unsigned 0 to 65535
    MEDIUMINT() --> Signed range -8388608 to 8388607, unsigned 0 to 16777215
    Int() -->Signed range -8388608 to 8388607, unsigned 0 to 4294967295.
    BIGINT() --> Signed range -9223372036854775808 to 9223372036854775807, unsigned range 0 to 18446744073709551615
    Float(precision,scale)
    Decimal(precision,scale)
    Double(precision,scale)
Date Data Types:
	Date --> used to add date format values. Format--> YYYY-MM-DD. Range is from '1000-01-01' to '9999-12-31'
    DateTime --> used to store date time combination. Format --> YYYY-MM-DD hh:mm:ss, range '1000-01-01 00:00:00' to '9999-12-31 23:59:59'.
    Time --> to store the time values
    Year --> used to store 4 digit year format. Values allowed in four-digit format: 1901 to 2155.
*/

/*
Constraints: 
	Primary Key: Combination of unique and not null values.
		--> A table consists only one primary key but it can be combination of multiple columns
		-- Creating a primary key
			create table table_name(
				col1_name datatype(size) constraints,
                col2_name ,
                .....
                primary key(col1_name)
			);
		-- Naming of primary key constraints on multiple columns
			create table table_name(
				col1_name datatype(size) constraints,
                col2_name datatype(size) constriants,
                .....
                primary key(col1_name,col2_name)
			);
            
            CREATE TABLE Persons (
				col1 datatype(size) constraint,
				col2 datatype(size) constraint,
				...............
				CONSTRAINT PK_name PRIMARY KEY (col1,col2)
			); 
		--> To create primary key constraints on the column when table is already created
			Alter table table_name
            add primary key(column_name);
            
			--> Defining primary key cosntraints on multiple columns by 
				Alter table table_name
				add constraint pk_name primary key(col1,col2);
							or
				Alter table table_name
				add primary key(col1,col2);
				(to declare column as primary after creation of table the column should not contain null values)
				
			--> To drop the primary key
				Alter table table_name
				drop primary key;
					or
				Alter table table_name
				drop constraint pk_name;
				
	Foreign Key: used to make a relation with multiple tables and prevents invalid data to get inserted into foreign key column 
		--> table can contain multiple foreign keys
		--> creating a foreign key 
			create table teble_name(
				col1 datatype(size) constraints,
                col2 datatype(size) constraints,
                .....
                foreign key (col_name) references parent_table(col_name)
			);
            
		--> naming of foreign constraints on multiple columns
			create table teble_name(
				col1 datatype(size) constraints,
                col2 datatype(size) constraints,
                .....
                foreign key (col1_name,col2_name) references parent_table(col1_name,col2_name)
			);
					or
			create table teble_name(
				col1 datatype(size) constraints,
                col2 datatype(size) constraints,
                .....
                constraint FK_name foreign key (col1_name,col2_name) references parent_table(col1_name,col2_name)
			);
            
            Example: 
				-- Departments table
					CREATE TABLE Departments (
						DepartmentID int,
						Location varchar(255),
						DepartmentName varchar(255),
						PRIMARY KEY (DepartmentID, Location)
					);

					-- Employees table
					CREATE TABLE Employees (
						EmployeeID int PRIMARY KEY,
						EmployeeName varchar(255),
						DepartmentID int,
						Location varchar(255),
						FOREIGN KEY (DepartmentID, Location) REFERENCES Departments(DepartmentID, Location)
					);
		
		--> Foreign Key on alter table after creating the table
			Alter table table_name
            add foreign key (col_name) references table_name(col_name);
            
            --> naming of foreign key constraint:
            ALter table table_name
            add constraint fk_name foreign key (column_names) references table_name(column_names); 
            
		--> TO drop the foreign key
        Alter table table_name
        drop foreign key;
        
        Alter table table_name
        drop foreign key generated Fk_name;
	
    Check() --> works on a condition based, it can be used to limit a value range to get inserted in a column
        Syntax: 
			create table table_name(
				col1 datatype(size) constraints,
                col2 datatype(size) constraints,
                ....
                check (col1--condition)
			);
		--> naming the constraint
			create table table_name(
				col1 datatype(size) constraints,
                col2 datatype(size) constraints,
                ....
                constraint chk_name check (col1--condition and col2--condition)
			);
		
        --> check with alter table
			Alter table table_name
            add Check (col_namae - condition);
				or
			Alter table table_name
            add constraint chk_name Check (col_name -- condition);
		--> to drop the check 
			Alter table table_name
            drop check chk_name;
		
	Default constraint: used to set the default value for a column
		--> Syntax:
			create table table_name(
				col1 datatype(size) constraints,
                col2 datatype(size) default <default_value>,
                .....
			);
		
        --> alter table to add default
			Alter table table_name
			alter col_name set default <default value>;
        
        --> to drop the default 
			Alter table table_name
            alter column_name drop deault;
	
	Auto Increment: allows to generate a unique number automatically
		--> Syntax:
			create table table_name(
				col1 datatype(size) AUTO_INCREMENT,
                ,.....
			);
		--> to set particular value for auto_increment
			create table table_name(
				col1 datatype(size) AUTO_INCREMENT,
                ,.....
                )AUTO_INCREMENT = 100;
                
		--> with alter table
			alter table table_name 
            Auto_increment = 100;
*/