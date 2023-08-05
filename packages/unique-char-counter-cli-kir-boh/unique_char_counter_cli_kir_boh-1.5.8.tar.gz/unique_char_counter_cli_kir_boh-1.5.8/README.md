Hello there!
Since you installed my module, you shoud know possibilities

#First unique_char_counter_cli.py:
```
By imorting unique_char_counter_cli.py from unique_char_counter_cli_kir_boh, you will be able to use four functions:
 
    return_amount_once_occured_items - gets hashable obj, cache it, count unique items deespite indentations.
    
    get_obj_from_cli - The get_obj_from_cli function takes no arguments and returns a namespace object generated from
        parsing command line arguments using the argparse module. It expects the user to pass either a string or a file
        containing a hashable object. The function uses mutually exclusive arguments, so the user can only pass either the 
        string or the file, but not both. The hashable object is the only mandatory argument, which is obtained from the 
        command line.
    
    read_file_in_chunks - reed file in chanks not to take a lot memory, gets two atrib 'path_to_file' (hasahable_obj) and
        chunck_size (by defoult chunck_size=1000)
    
    main - gets args from 'get_obj_from_cli', wich should be either file or string and hashable obj, then if it's fille,
        it will execute 'read_file_in_chunks' then 'return_amount_once_occured_items' to return and print result

Hint: To use main you should import main from unique_char_counter_cli.py and run 'python main.py -s <hasable object>' 
in the sane directory      
```
#tests package:
```
By imorting tests_unique_char_counter_cli.py from unique_char_counter_cli_kir_boh.tests you get the pyton file with 
TestUniqueCharCounterCli class wich inheritate from unittest.TestCase. After imporing, it is used as parent class
        
    The test_return_amount_once_occured_items_with_string, test_return_amount_once_occured_items_with_empty_string,
        test_return_amount_once_occured_items_with_space, and test_return_amount_once_occured_items_with_unhashable_obj 
        methods test the return_amount_once_occured_items function with different inputs.
        
    The `test_main_with_mock_file` methods test the `main` function with different inputs using the `mock_open` and 
        `mock_get_obj_from_cli` decorators.
        
    The `test_read_file_in_chunks` method tests the `read_file_in_chunks` function with a file input.
```