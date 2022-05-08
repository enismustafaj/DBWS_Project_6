select * from clothes;
select * from `keys`;
select * from earphone;
select * from campus_card;
select * from lost_and_found;
select * from person;
select * from Moderator_Moderates_Lost_and_Found;
--get the items which have been claimed or not.
select * from lost_and_found  join item on lost_and_found.Specific_ITEM_ID = item.ITEM_ID and claimed = 1;
select * from lost_and_found  join item on lost_and_found.Specific_ITEM_ID = item.ITEM_ID and claimed = 0;

--get every specific item related to the person who lost or found it
select `Given_Name`, Surname, `Status`, email, `Person_HAS_ID` from person join Person_has_Item on Person_has_Item.Person_email = person.email;
select * from item join (select `Given_Name`, Surname, `Status`, email, `Person_HAS_ID` from person join Person_has_Item on Person_has_Item.Person_email = person.email) as tab on tab.Person_Has_ID = item.ITEM_ID;

--get the people who lost or found items togesther with the specific item
select * from item join (select `Given_Name`, Surname, `Status`, email, `Person_HAS_ID` from person join Person_has_Item on Person_has_Item.Person_email = person.email) as tab on tab.Person_Has_ID = item.ITEM_ID and tab.status = 'lost';
select * from item join (select `Given_Name`, Surname, `Status`, email, `Person_HAS_ID` from person join Person_has_Item on Person_has_Item.Person_email = person.email) as tab on tab.Person_Has_ID = item.ITEM_ID and tab.status = 'found';

--get the number of items lost in the past 2 months
select count(*) from lost_and_found where DATE_SUB(now(), INTERVAL 60 DAY) < `Lost_Date` and `Lost_Date` != '0000-00-00';

--get the items that a moderator deleted 
select * from person join Moderator_Moderates_Lost_and_Found on Moderator_Moderates_Lost_and_Found.Moderator_Person_email = person.email;
select * from lost_and_found join (select * from person join Moderator_Moderates_Lost_and_Found on Moderator_Moderates_Lost_and_Found.Moderator_Person_email = person.email) as tab on tab.Lost_and_Found_Specific_ITEM_ID = lost_and_found.Specific_ITEM_ID;

--get the data related to a specific person of his/her item grouped by the status
select `Given_Name`, Surname, `Status`, email, `Person_HAS_ID` from person join Person_has_Item where  person.email = 'SalmaHenry@jacobs-university.de' and person.email = Person_has_Item.Person_email group by `status`;

--update the lost and found table if someone claimed its own item
update lost_and_found set claimed = 1 where Specific_ITEM_ID = 111;

--delete an item form the lost and found table if the item is invalid
delete from lost_and_found where Specific_ITEM_ID = 111;


