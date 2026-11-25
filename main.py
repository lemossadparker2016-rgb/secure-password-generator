import secrets
import string

def generate_password(length=12, use_symbols=True):
    """Génère un mot de passe aléatoire hautement sécurisé."""
    # Alphabet de base (lettres et chiffres)
    alphabet = string.ascii_letters + string.digits
    
    # Ajout des symboles si demandé
    if use_symbols:
        alphabet += string.punctuation
        
    # Utilisation de 'secrets' pour une génération cryptographique
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    try:
        length_input = input("Enter password length (default is 12): ")
        length = int(length_input) if length_input.strip() else 12
        
        symbols_input = input("Include special symbols? (y/n, default is y): ").lower()
        use_symbols = symbols_input != 'n'
        
        print("\nGenerating...")
        secure_pwd = generate_password(length, use_symbols)
        # Le code \033[1;32m colore le texte en vert dans le terminal
        print(f"Your new secure password is: \033[1;32m{secure_pwd}\033[0m") 
        
    except ValueError:
        print("Error: Please enter a valid number for the length.")
