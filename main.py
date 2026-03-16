import os
import sys
import traceback
import time
from types import ModuleType
import torch
import torch.nn.functional as F

# =====================================================================
# EL CEREBRO SINTÉTICO (FAKE XFORMERS COMPLETO)
# =====================================================================
os.environ["ACCELERATE_USE_XFORMERS"] = "FALSE"

fake_xformers = ModuleType('xformers')
fake_ops = ModuleType('xformers.ops')
fake_fmha = ModuleType('xformers.ops.fmha')
fake_attn_bias = ModuleType('xformers.ops.fmha.attn_bias')

class DummyMask:
    @classmethod
    def from_seqlens(cls, *args, **kwargs): return cls()

fake_ops.LowerTriangularMask = DummyMask
fake_attn_bias.BlockDiagonalCausalMask = DummyMask
fake_fmha.attn_bias = fake_attn_bias
fake_ops.fmha = fake_fmha

def fake_memory_efficient_attention(query, key, value, attn_bias=None, p=0.0, scale=None):
    q = query.transpose(1, 2)
    k = key.transpose(1, 2)
    v = value.transpose(1, 2)
    is_causal = (attn_bias is not None)
    out = F.scaled_dot_product_attention(
        q, k, v,
        attn_mask=None,
        dropout_p=p if p is not None else 0.0,
        is_causal=is_causal,
        scale=scale
    )
    return out.transpose(1, 2)

fake_ops.memory_efficient_attention = fake_memory_efficient_attention
fake_ops.unbind = torch.unbind 

sys.modules['xformers'] = fake_xformers
sys.modules['xformers.ops'] = fake_ops
sys.modules['xformers.ops.fmha'] = fake_fmha
sys.modules['xformers.ops.fmha.attn_bias'] = fake_attn_bias

# =====================================================================
# DICCIONARIOS DEL SISTEMA MODULAR
# =====================================================================
MODULES = {
    "genre": ["hip hop", "trap", "drill", "boom bap", "lo fi hip hop", "cinematic hip hop", "experimental hip hop", "ambient hip hop", "future hip hop", "reggaeton"],
    "subgenre": ["dark trap", "emotional hip hop", "epic cinematic hip hop", "ambient trap", "underground boom bap", "melancholic trap", "futuristic trap", "cyber hip hop", "lofi chill hop", "industrial hip hop", "classic reggaeton", "perreo pesado", "reggaeton romantico", "neoperreo", "trapeton", "moombahton"],
    "mood": ["dark", "mysterious", "ominous", "tense", "aggressive", "melancholic", "nostalgic", "reflective", "dramatic", "powerful", "confident", "determined", "uplifting", "epic", "grand", "intense", "cyberpunk", "digital", "synthetic", "sci-fi"],
    "drums": ["punchy hip hop drums", "hard trap drums", "minimal lofi drums", "aggressive drill drums", "cinematic hybrid drums", "boom bap sampled drums", "modern digital trap drums", "classic dembow rhythm", "modern reggaeton drums"],
    "hihat": ["fast trap rolls", "triplet hi hats", "minimal hip hop hats", "glitch hats", "swing boom bap hats", "stutter hi hats", "double time hi hats"],
    "bass": ["deep 808 bass", "distorted 808", "sub bass", "analog bass", "cinematic hybrid bass", "glide 808 bass"],
    "melody": ["dark piano", "emotional piano", "ambient synth pads", "analog synth lead", "cinematic strings", "ethnic instruments", "electric guitar melodies", "lofi sampled keys", "choir pads"],
    "atmosphere": ["dark ambient textures", "urban night ambience", "cinematic sound design", "ethereal pads", "industrial textures", "vinyl noise ambience", "analog tape ambience", "digital glitch textures"],
    "structure": [
        "intro -> build up -> drop -> breakdown -> second drop -> outro",
        "ambient intro -> rhythm entry -> main groove -> breakdown -> final drop",
        "atmospheric intro -> cinematic build -> impact drop -> final epic drop"
    ],
    "production": ["modern hip hop mix", "wide stereo cinematic mix", "heavy bass mastering", "clean punchy drums mix", "lofi analog saturation mix", "dark trap mix", "high clarity digital mix", "vintage analog hip hop mix"],
    "special_fx": ["reverse transitions", "risers", "impacts", "glitch fx", "vinyl textures", "radio filter effects", "tape stop effects", "cinematic booms"],
    "context": ["underground rap cypher", "90s block party", "late night studio session", "graffiti yard tagging", "skatepark montage", "lowrider cruising", "gritty street corner freestyle", "abandoned warehouse", "vinyl record store digging", "smoky underground club", "street basketball game"]
}

import customtkinter as ctk
import scipy.io.wavfile as wavfile
import threading

from audiocraft.models import MusicGen

# =====================================================================
# PALETA DE COLORES DINÁMICA
# =====================================================================
C_BG_MAIN = ("#FFFFFF", "#121212")        
C_BG_PANEL = ("#F0F8FF", "#1E1E1E")       
C_TEXT_DARK = ("#102A43", "#FFFFFF")      
C_CELESTE_BTN = ("#E0F0FF", "#2A2A2A")    
C_CELESTE_HOVER = ("#CCE4FF", "#3A3A3A")  
C_ACCENT_BLUE = ("#3388FF", "#FF4500")    
C_NEON_GREEN = ("#39ff14", "#39ff14")     
C_DARK_PILL = ("#102A43", "#000000")      

FONT_FAMILY = "Segoe UI"

class HiphopBeatsMachine(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EDUARDO FIERRO DUQUE BEATS MACHINE V.3 MODULAR SYSTEM")
        self.geometry("900x900") # Un poco más ancho para acomodar los nuevos botones
        self.minsize(750, 700) 
        
        ctk.set_appearance_mode("light")
        self.configure(fg_color=C_BG_MAIN)
        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = None
        self.is_generating = False
        self.vars = {}
        
        # --- SISTEMA DE COLA Y CONTROL DE TRÁFICO ---
        self.beat_queue = []
        self.simulate_progress_active = False
        self.is_paused = False
        self.cancel_requested = False

        # --- BARRA SUPERIOR ---
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.pack(fill="x", padx=30, pady=(20, 10))
        top_frame.grid_columnconfigure(0, weight=1)
        
        self.label = ctk.CTkLabel(
            top_frame, text="EDUARDO FIERRO DUQUE BEATS MACHINE V.3\nMODULAR SYSTEM", 
            font=(FONT_FAMILY, 22, "bold"), text_color=C_TEXT_DARK, justify="left"
        )
        self.label.grid(row=0, column=0, sticky="w")
        
        self.theme_switch = ctk.CTkSwitch(
            top_frame, text="Modo Oscuro", font=(FONT_FAMILY, 12, "bold"), text_color=C_TEXT_DARK,
            command=self.toggle_theme, progress_color=C_ACCENT_BLUE
        )
        self.theme_switch.grid(row=0, column=1, sticky="e")

        # --- DURACIÓN ---
        self.duration_var = ctk.StringVar(value="30 Seg")
        self.duration_selector = ctk.CTkSegmentedButton(
            self, values=["30 Seg", "1 Minuto"], variable=self.duration_var,
            selected_color=C_ACCENT_BLUE, selected_hover_color="#2266CC",
            unselected_color=C_CELESTE_BTN, unselected_hover_color=C_CELESTE_HOVER,
            text_color=C_TEXT_DARK,
            font=(FONT_FAMILY, 13, "bold")
        )
        self.duration_selector.pack(pady=5)

        # --- PANEL DESPLAZABLE ---
        self.scroll_frame = ctk.CTkScrollableFrame(
            self, fg_color=C_BG_PANEL, corner_radius=15
        )
        self.scroll_frame.pack(pady=10, fill="both", expand=True, padx=20)
        
        self.scroll_frame.grid_columnconfigure(0, weight=1)
        self.scroll_frame.grid_columnconfigure(1, weight=1)

        # --- TEMPO (BPM) ---
        bpm_frame = ctk.CTkFrame(self.scroll_frame, fg_color=C_DARK_PILL, corner_radius=10)
        bpm_frame.grid(row=0, column=0, columnspan=2, pady=(15, 25), padx=20, sticky="ew")
        
        self.bpm_label = ctk.CTkLabel(
            bpm_frame, text="TEMPO (BPM): 90", 
            font=(FONT_FAMILY, 15, "bold"), text_color=C_NEON_GREEN
        )
        self.bpm_label.pack(pady=(10, 5))
        
        self.bpm_slider = ctk.CTkSlider(
            bpm_frame, from_=60, to=150, 
            command=self.update_bpm_label, 
            progress_color=C_NEON_GREEN, button_color=C_NEON_GREEN, button_hover_color="#FFFFFF"
        )
        self.bpm_slider.set(90)
        self.bpm_slider.pack(fill="x", expand=True, padx=40, pady=(0, 15))

        # --- MÓDULOS EN 2 COLUMNAS ---
        self.create_dropdown("1. GENRE", "genre", MODULES["genre"], row=1, col=0)
        self.create_dropdown("2. SUBGENRE", "subgenre", MODULES["subgenre"], row=1, col=1)
        self.create_dropdown("3. MOOD", "mood", MODULES["mood"], row=2, col=0)
        self.create_dropdown("4. DRUM STYLE", "drums", MODULES["drums"], row=2, col=1)
        self.create_dropdown("5. HI-HAT PATTERN", "hihat", MODULES["hihat"], row=3, col=0)
        self.create_dropdown("6. BASS TYPE", "bass", MODULES["bass"], row=3, col=1)
        self.create_dropdown("7. MELODIC ELEMENT", "melody", MODULES["melody"], row=4, col=0)
        self.create_dropdown("8. ATMOSPHERE", "atmosphere", MODULES["atmosphere"], row=4, col=1)
        self.create_dropdown("9. STRUCTURE", "structure", MODULES["structure"], row=5, col=0)
        self.create_dropdown("10. PRODUCTION STYLE", "production", MODULES["production"], row=5, col=1)
        self.create_dropdown("11. SPECIAL FX", "special_fx", MODULES["special_fx"], row=6, col=0)
        self.create_dropdown("12. CONTEXT (Vibe)", "context", MODULES["context"], row=6, col=1)

        # --- ÁREA DE CONTROL INFERIOR MAESTRA ---
        bottom_controls = ctk.CTkFrame(self, fg_color="transparent")
        bottom_controls.pack(pady=5)
        
        # 1. Botón Añadir a la Cola
        self.btn_queue = ctk.CTkButton(
            bottom_controls, text="➕ AÑADIR A LA COLA", font=(FONT_FAMILY, 14, "bold"), 
            fg_color=C_ACCENT_BLUE, hover_color="#2266CC", height=45,
            command=self.add_to_queue
        )
        self.btn_queue.grid(row=0, column=0, padx=10)

        # 2. Botón Pausar/Reanudar
        self.btn_pause = ctk.CTkButton(
            bottom_controls, text="⏸ PAUSAR", font=(FONT_FAMILY, 14, "bold"), 
            fg_color="#F39C12", hover_color="#D68910", height=45, state="disabled",
            command=self.toggle_pause
        )
        self.btn_pause.grid(row=0, column=1, padx=10)

        # 3. Botón Cancelar
        self.btn_cancel = ctk.CTkButton(
            bottom_controls, text="⏹ CANCELAR", font=(FONT_FAMILY, 14, "bold"), 
            fg_color="#E74C3C", hover_color="#C0392B", height=45, state="disabled",
            command=self.cancel_generation
        )
        self.btn_cancel.grid(row=0, column=2, padx=10)

        # 4. Botón Generar (Fuego)
        self.btn_generate = ctk.CTkButton(
            bottom_controls, text="🔥", 
            font=("Segoe UI Emoji", 40),     
            text_color="#FF4500",            
            fg_color="transparent", 
            hover_color=C_CELESTE_BTN, 
            text_color_disabled="gray",      
            width=60, command=self.start_generation
        )
        self.btn_generate.grid(row=0, column=3, padx=10)

        # Indicador de Cola
        self.queue_label = ctk.CTkLabel(
            self, text="Tracks en cola: 0", 
            font=(FONT_FAMILY, 14, "bold"), text_color="#7A8B99"
        )
        self.queue_label.pack(pady=(0, 5))

        self.progress_bar = ctk.CTkProgressBar(
            self, width=350, height=10, 
            progress_color=C_ACCENT_BLUE, fg_color=C_CELESTE_BTN
        )
        self.progress_bar.set(0)
        self.progress_bar.pack_forget() 

        self.status_label = ctk.CTkLabel(
            self, text=f"Motor: Listo | Arquitectura Modular Activa", 
            font=(FONT_FAMILY, 12), text_color="#7A8B99"
        )
        self.status_label.pack(pady=5)

    def toggle_theme(self):
        if self.theme_switch.get() == 1:
            ctk.set_appearance_mode("dark")
            self.theme_switch.configure(text="Modo Claro")
            self.btn_queue.configure(fg_color=C_ACCENT_BLUE[1], hover_color="#CC3700")
        else:
            ctk.set_appearance_mode("light")
            self.theme_switch.configure(text="Modo Oscuro")
            self.btn_queue.configure(fg_color=C_ACCENT_BLUE[0], hover_color="#2266CC")

    def create_dropdown(self, title, dict_key, options_list, row, col):
        frame = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
        frame.grid(row=row, column=col, padx=20, pady=10, sticky="ew")

        label = ctk.CTkLabel(
            frame, text=title, font=(FONT_FAMILY, 11, "bold"), text_color=C_TEXT_DARK
        )
        label.pack(anchor="w")
        
        var = ctk.StringVar(value=options_list[0])
        self.vars[dict_key] = var
        
        menu = ctk.CTkOptionMenu(
            frame, values=options_list, variable=var,
            fg_color=C_CELESTE_BTN, button_color=C_CELESTE_HOVER, button_hover_color=C_ACCENT_BLUE, 
            text_color=C_TEXT_DARK, font=(FONT_FAMILY, 13), corner_radius=6
        )
        menu.pack(fill="x", pady=(2, 0))

    def update_bpm_label(self, value):
        self.bpm_label.configure(text=f"TEMPO (BPM): {int(value)}")

    # ==========================================
    # LÓGICA DE CONTROL MAESTRO (Añadir, Pausar, Cancelar)
    # ==========================================
    def add_to_queue(self):
        bpm_val = int(self.bpm_slider.get())
        duration_seconds = 30 if self.duration_var.get() == "30 Seg" else 60
        
        prompt = (
            f"Pure instrumental track. "
            f"Genre: {self.vars['genre'].get()}, Subgenre: {self.vars['subgenre'].get()}. "
            f"Mood: {self.vars['mood'].get()}. Tempo: {bpm_val} BPM. "
            f"Rhythm: {self.vars['drums'].get()}, Hi-hats: {self.vars['hihat'].get()}. "
            f"Instrumentation - Bass: {self.vars['bass'].get()}, Melody: {self.vars['melody'].get()}. "
            f"Atmosphere: {self.vars['atmosphere'].get()}. "
            f"Structure: {self.vars['structure'].get()}. "
            f"Production: {self.vars['production'].get()}. "
            f"Special FX: {self.vars['special_fx'].get()}. "
            f"Context: {self.vars['context'].get()}."
        )
        
        base_name = f"beat_modular_{self.vars['genre'].get().replace(' ', '')}"
        
        self.beat_queue.append({
            "prompt": prompt,
            "duration": duration_seconds,
            "base_name": base_name
        })
        
        self.queue_label.configure(text=f"Tracks en cola: {len(self.beat_queue)}")
        color_exito = "#FF4500" if self.theme_switch.get() == 1 else "#3388FF"
        self.status_label.configure(text="¡Beat guardado en la cola!", text_color=color_exito)

    def toggle_pause(self):
        if self.is_paused:
            self.is_paused = False
            self.btn_pause.configure(text="⏸ PAUSAR", fg_color="#F39C12", hover_color="#D68910")
            self.status_label.configure(text="Generación reanudada...", text_color="#3388FF")
        else:
            self.is_paused = True
            self.btn_pause.configure(text="▶ REANUDAR", fg_color="#2ECC71", hover_color="#27AE60")
            self.status_label.configure(text="Cola pausada (El track actual terminará antes de detenerse)", text_color="#F39C12")

    def cancel_generation(self):
        self.cancel_requested = True
        self.beat_queue.clear()
        self.queue_label.configure(text="Tracks en cola: 0")
        self.status_label.configure(text="Cancelando... (El track actual terminará y el motor se detendrá)", text_color="#E74C3C")
        self.btn_pause.configure(state="disabled")

    def start_generation(self):
        if self.is_generating: return
        
        if len(self.beat_queue) == 0:
            self.add_to_queue()
            
        self.is_generating = True
        self.cancel_requested = False
        self.is_paused = False
        
        # Activar/Desactivar controles pertinentes
        self.btn_generate.configure(state="disabled")
        self.btn_queue.configure(state="disabled")
        self.btn_pause.configure(state="normal", text="⏸ PAUSAR", fg_color="#F39C12")
        self.btn_cancel.configure(state="normal")
        
        threading.Thread(target=self.process_queue, daemon=True).start()

    def simulate_progress(self, duration):
        if not self.simulate_progress_active: return
        current = self.progress_bar.get()
        increment = 0.015 if duration == 30 else 0.007
        if current < 0.9:
            self.progress_bar.set(current + increment)
            self.after(500, lambda: self.simulate_progress(duration))

    def process_queue(self):
        try:
            if self.model is None:
                self.status_label.configure(text="Cargando motor IA (Solo la primera vez)...", text_color="#FF4500")
                self.model = MusicGen.get_pretrained('facebook/musicgen-large')
            
            total_tracks = len(self.beat_queue)
            current_track_num = 1
            
            # EL BUCLE DE PRODUCCIÓN INTELIGENTE
            while len(self.beat_queue) > 0:
                # 1. Comprobar si hay solicitud de cancelación
                if self.cancel_requested:
                    break
                
                # 2. Comprobar si el usuario pausó el proceso
                while self.is_paused and not self.cancel_requested:
                    time.sleep(1)
                
                # Segunda comprobación por si el usuario canceló mientras estaba pausado
                if self.cancel_requested:
                    break

                # 3. Extraer el track y procesarlo
                task = self.beat_queue.pop(0) 
                self.queue_label.configure(text=f"Tracks en cola: {len(self.beat_queue)}")
                self.status_label.configure(text=f"Procesando Track {current_track_num}... 🔥", text_color="#FF4500")
                
                self.progress_bar.pack(pady=5, before=self.status_label)
                self.progress_bar.set(0)
                
                self.simulate_progress_active = True
                threading.Thread(target=self.simulate_progress, args=(task['duration'],), daemon=True).start()
                
                self.model.set_generation_params(
                    duration=task['duration'],
                    cfg_coef=6.0, 
                    top_k=250            
                )
                
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()

                with torch.inference_mode():
                    wav = self.model.generate([task['prompt']])
                
                if not os.path.exists("exports"): os.makedirs("exports")
                
                counter = 1
                path = f"exports/{task['base_name']}_{counter}.wav"
                while os.path.exists(path):
                    counter += 1
                    path = f"exports/{task['base_name']}_{counter}.wav"
                
                wav_data = wav[0].cpu().numpy()[0]
                wavfile.write(path, 32000, wav_data)
                
                self.simulate_progress_active = False
                self.progress_bar.set(1.0)
                current_track_num += 1
                time.sleep(1) 
                
            if self.cancel_requested:
                self.status_label.configure(text="Proceso cancelado por el usuario.", text_color="#E74C3C")
            else:
                self.status_label.configure(text=f"¡Lote terminado exitosamente!", text_color="#28A745")
            
        except Exception as e:
            self.status_label.configure(text="Error de procesamiento.", text_color="red")
            traceback.print_exc()
        finally:
            # RESETEO DE SISTEMA Y BOTONES AL TERMINAR
            self.simulate_progress_active = False
            self.is_generating = False
            self.cancel_requested = False
            self.is_paused = False
            
            self.btn_pause.configure(state="disabled", text="⏸ PAUSAR", fg_color="#F39C12")
            self.btn_cancel.configure(state="disabled")
            self.btn_generate.configure(state="normal")
            self.btn_queue.configure(state="normal")
            self.after(5000, self.progress_bar.pack_forget)

if __name__ == "__main__":
    app = HiphopBeatsMachine()
    app.mainloop()