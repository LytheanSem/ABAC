/*
Examples to create tables for BankDB
*/
create table branch (
  branch_name char(15),
  branch_city char(15),
  assets numeric(18,2)
);

create table customer (
	customer_name	char(15),
    customer_street	char(15),
    customer_city	char(15)
);

create table account (
    account_number 	char(10),
	branch_name		char(15),
	balance			numeric(18,2)
);

create table depositor (
    customer_name	char(15),
    account_number 	char(10)
);

create table loan (
	loan_number 	char(10),
    branch_name		char(15),
	amount			numeric(18,2)
);

create table borrower (
    customer_name	char(15),
    loan_number 	char(10)
);