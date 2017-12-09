CREATE TRIGGER update_qty AFTER INSERT ON myapp_orders 
	FOR EACH ROW 
		UPDATE myapp_book SET numberOfCopies = numberOfCopies - NEW.quantityOrdered
        WHERE ISBN13 = NEW.ISBN13