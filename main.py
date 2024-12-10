import importlib	
from lib.get_user_input import get_user_input	
from lib.validate_input import validate_input	


base_map = {	
    'd': "decimal",	
    'b': "binary",	
    'o': "octal",	
    'h': "hexadecimal"	
}	

def main():	
    print("\nWelcome to the Number Base System Converter!")	
    print("Available bases:\nDecimal(d)\nBinary(b)\nOctal(o)\nHexadecimal(h)")	

    while True:	
        from_base = get_user_input("Enter the base you want to convert from (d, b, o, h): ", base_map.keys())	

        while True:	
            value = input(f"Enter the value you want to convert from {base_map[from_base]}: ").strip()	
            try:	
                validate_input(value, from_base)	
                break	
            except ValueError as e:	
                print(e)	


        while True:	
            to_base = get_user_input("Enter the base you want to convert to (d, b, o, h): ", base_map.keys())	
            if(to_base != from_base):	
                break	
            print(f"You cannot convert to the same base, {base_map[from_base]} to {base_map[to_base]}")	

        print(f"Converting {value} from {base_map[from_base]} to {base_map[to_base]}...")	

        file_and_func_name = base_map[from_base] + '_to_' + base_map[to_base]	

        try:	
            module = importlib.import_module(f"lib.converters.{file_and_func_name}")	

            func = getattr(module, file_and_func_name)	

            result = func(value)	
            print("Result:", result)	

        except ModuleNotFoundError:	
            print(f"Error: Conversion file 'lib/{file_and_func_name}.py' not found.")	
        except AttributeError:	
            print(f"Error: Function '{file_and_func_name}' not found in 'lib/{file_and_func_name}.py'.")	
        except ValueError as e:	
            print(f"Value Error: {e}")	
        except Exception as e:	
            print(f"An unexpected error occurred: {e}")	

        retry = get_user_input("Do you want to perform another conversion? (y/n): ", ['y', 'n'])	
        if retry == 'n':	
            print("Goodbye!")	
            break	

if __name__ == "__main__":	
    main()
