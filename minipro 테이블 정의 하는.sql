DROP TABLE disease;
DROP TABLE prod;
DROP TABLE users;
DROP TABLE userdis;
DROP TABLE usermiddle;
DROP TABLE naver_table;



CREATE TABLE users(
    user_id VARCHAR2(50) not null,
    user_pw VARCHAR2(20) not null,
    user_age VARCHAR2(15) not null,
    user_gender VARCHAR2(15) not null,
    user_stress VARCHAR2(30) not null,
    CONSTRAINT users_pk PRIMARY KEY (user_id)
);

INSERT INTO users(user_id, user_pw, user_age, user_gender, user_stress) VALUES('sungsam97@naver.com','dbdb','20대', '남자', '많음');

CREATE TABLE disease (
    dis_rank VARCHAR2(500) not null,
    dis_code VARCHAR2(500) not null,
    dis_top VARCHAR2(300) not null,
    dis_m_num NUMBER(10) NOT NULL,
    dis_middle VARCHAR2(300) not null,
    dis_id VARCHAR2(1000) not null,
    dis_age1 VARCHAR2(50) not null,
    dis_age2 VARCHAR2(50) not null,
    dis_age3 VARCHAR2(50) not null,
    dis_gender VARCHAR2(10),
    CONSTRAINT disease_pk PRIMARY KEY (dis_id, dis_middle)
);

CREATE TABLE userdis (
    ud_id VARCHAR2(50) NOT NULL,
    ud_dis VARCHAR2(50),
    CONSTRAINT userdis_pk PRIMARY KEY (ud_id, ud_dis),
    CONSTRAINT userdis_fk_user FOREIGN KEY (ud_id) REFERENCES users(user_id)
);

CREATE TABLE usermiddle (
    md_id VARCHAR2(50) NOT NULL,
    md_middle VARCHAR2(50),
    CONSTRAINT usermiddle_pk PRIMARY KEY (md_id, md_middle),
    CONSTRAINT usermiddle_fk_user FOREIGN KEY (md_id) REFERENCES users(user_id)
);

DROP TABLE prod;


CREATE TABLE Prod (
    prod_name VARCHAR2(300) NOT NULL,
    prod_eff VARCHAR2(300),
    prod_m_num VARCHAR2(10),    
    prod_max VARCHAR2(300),
    prod_min VARCHAR2(300),
    prod_unit VARCHAR2(10),
    prod_warn VARCHAR2(900),
    prod_middle VARCHAR2(500),
    CONSTRAINT prod_pk PRIMARY KEY (prod_name, prod_m_num)
);

CREATE TABLE naver_table (
    rank NUMBER,
    Keyword VARCHAR2(255),
    age1 VARCHAR2(255),
    age2 VARCHAR2(255),
    age3 VARCHAR2(255)
);

