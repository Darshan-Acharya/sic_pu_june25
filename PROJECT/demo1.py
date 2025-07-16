import tkinter as tk
from tkinter import ttk, scrolledtext
import random
import time

class RailGuardProApp:
    def __init__(self, master):
        self.master = master
        master.title("RailGuard Pro - Anti-Stampede System")
        master.geometry("1200x800")
        master.configure(bg='#f0f2f5') # Light gray background

        # Configure styles for ttk widgets
        style = ttk.Style()
        style.theme_use('clam') # 'clam', 'alt', 'default', 'classic'
        
        # General TFrame style for white background
        style.configure('TFrame', background='#ffffff', relief='flat', borderwidth=0)
        # Style for the header frame with blue background
        style.configure('Header.TLabel', font=('Inter', 18, 'bold'), foreground='white', background='#4a90e2')
        # Style for main labels within frames
        style.configure('TLabel', background='#ffffff', foreground='#333333', font=('Inter', 10))
        # Style for density labels on the map
        style.configure('Density.TLabel', font=('Inter', 12, 'bold'), foreground='white', padding=5, relief='raised', borderwidth=2, bordercolor='white')
        # Style for section titles
        style.configure('Section.TLabel', font=('Inter', 14, 'bold'), foreground='#333333')
        # Style for map frame background
        style.configure('Map.TFrame', background='#e0e0e0')


        # Header Frame
        header_frame = ttk.Frame(master, style='TFrame', padding="15 10")
        header_frame.pack(fill=tk.X, pady=(10, 5), padx=10)
        # Apply the Header.TLabel style to the header_frame itself for background
        header_frame.configure(style='Header.TLabel')
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=0)

        header_label = ttk.Label(header_frame, text="RailGuard Pro - Anti-Stampede System", font=('Inter', 24, 'bold'), foreground='white', background='#4a90e2')
        header_label.grid(row=0, column=0, sticky=tk.W)

        time_label = ttk.Label(header_frame, text=f"Station: Central Terminus\n{time.strftime('%Y-%m-%d %H:%M:%S')}", font=('Inter', 10), foreground='white', background='#4a90e2')
        time_label.grid(row=0, column=1, sticky=tk.E)
        self.time_label = time_label # Store reference for updates

        # Main Content Frames
        main_content_frame = ttk.Frame(master, style='TFrame', padding=10)
        main_content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        main_content_frame.grid_columnconfigure(0, weight=2) # Dashboard Overview
        main_content_frame.grid_columnconfigure(1, weight=1) # Alerts & Ticket Data
        main_content_frame.grid_rowconfigure(0, weight=1) # Row for top sections
        main_content_frame.grid_rowconfigure(1, weight=1) # Row for camera feeds

        # --- Left Column: Dashboard Overview ---
        dashboard_frame = ttk.Frame(main_content_frame, style='TFrame', padding=15)
        dashboard_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=(0, 10), pady=0)
        dashboard_frame.grid_rowconfigure(1, weight=1) # Allow map to expand

        ttk.Label(dashboard_frame, text="Station Overview", font=('Inter', 18, 'bold'), foreground='#2a6496', background='white').pack(anchor=tk.NW, pady=(0, 10))

        # Simulated Station Map
        map_frame = ttk.Frame(dashboard_frame, style='Map.TFrame', relief=tk.SOLID, borderwidth=1, padding=10)
        map_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        map_frame.grid_rowconfigure(0, weight=1)
        map_frame.grid_rowconfigure(1, weight=1)
        map_frame.grid_rowconfigure(2, weight=1)
        map_frame.grid_columnconfigure(0, weight=1)
        map_frame.grid_columnconfigure(1, weight=1)
        map_frame.grid_columnconfigure(2, weight=1)

        self.density_labels = {}
        areas = [
            ("Entrance", 0, 1),
            ("Platform 1", 1, 0),
            ("Platform 2", 1, 2),
            ("Exit", 2, 1)
        ]
        for name, r, c in areas:
            label = ttk.Label(map_frame, text=f"{name} (0%)", style='Density.TLabel', anchor=tk.CENTER)
            label.grid(row=r, column=c, padx=5, pady=5, sticky=tk.NSEW)
            self.density_labels[name] = label

        # Central Concourse Placeholder
        ttk.Label(map_frame, text="Concourse Area", background='#cccccc', foreground='#666666', font=('Inter', 10), anchor=tk.CENTER).grid(row=1, column=1, padx=5, pady=5, sticky=tk.NSEW)


        # Key Metrics
        metrics_frame = ttk.Frame(dashboard_frame, style='TFrame', padding=10)
        metrics_frame.pack(fill=tk.X, pady=(0, 0))
        metrics_frame.grid_columnconfigure(0, weight=1)
        metrics_frame.grid_columnconfigure(1, weight=1)

        inflow_frame = ttk.Frame(metrics_frame, style='TFrame', padding=10, relief=tk.GROOVE, borderwidth=1)
        inflow_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=(0, 5))
        ttk.Label(inflow_frame, text="Total Station Inflow", font=('Inter', 12, 'bold'), foreground='#2a6496', background='white').pack(anchor=tk.NW)
        self.total_inflow_label = ttk.Label(inflow_frame, text="0", font=('Inter', 24, 'bold'), foreground='#2a6496', background='white')
        self.total_inflow_label.pack(anchor=tk.NW)

        waitlist_frame = ttk.Frame(metrics_frame, style='TFrame', padding=10, relief=tk.GROOVE, borderwidth=1)
        waitlist_frame.grid(row=0, column=1, sticky=tk.NSEW, padx=(5, 0))
        ttk.Label(waitlist_frame, text="Waitlisted Passengers Held", font=('Inter', 12, 'bold'), foreground='#6a0dad', background='white').pack(anchor=tk.NW)
        self.waitlisted_held_label = ttk.Label(waitlist_frame, text="0", font=('Inter', 24, 'bold'), foreground='#6a0dad', background='white')
        self.waitlisted_held_label.pack(anchor=tk.NW)

        # --- Right Column: Alerts & Ticket Data ---
        right_column_frame = ttk.Frame(main_content_frame, style='TFrame', padding=0)
        right_column_frame.grid(row=0, column=1, sticky=tk.NSEW, padx=(10, 0), pady=0)
        right_column_frame.grid_rowconfigure(0, weight=1) # Alerts
        right_column_frame.grid_rowconfigure(1, weight=1) # Ticket Data

        # Alerts Panel
        alerts_frame = ttk.Frame(right_column_frame, style='TFrame', padding=15)
        alerts_frame.grid(row=0, column=0, sticky=tk.NSEW, pady=(0, 10))
        alerts_frame.grid_rowconfigure(1, weight=1)
        alerts_frame.grid_columnconfigure(0, weight=1)

        ttk.Label(alerts_frame, text="Live Alerts", font=('Inter', 18, 'bold'), foreground='#cc0000', background='white').pack(anchor=tk.NW, pady=(0, 10))
        self.alerts_text = scrolledtext.ScrolledText(alerts_frame, wrap=tk.WORD, width=40, height=10, font=('Inter', 10), bg='#ffe6e6', fg='#333333', relief=tk.FLAT, borderwidth=0)
        self.alerts_text.pack(fill=tk.BOTH, expand=True)
        self.alerts_text.tag_config('CRITICAL', foreground='red', font=('Inter', 10, 'bold'))
        self.alerts_text.tag_config('WARNING', foreground='#e6b800', font=('Inter', 10))


        # Ticket Data Panel
        ticket_data_frame = ttk.Frame(right_column_frame, style='TFrame', padding=15)
        ticket_data_frame.grid(row=1, column=0, sticky=tk.NSEW, pady=(10, 0))
        ticket_data_frame.grid_columnconfigure(1, weight=1) # Allow values to expand

        ttk.Label(ticket_data_frame, text="Ticket Data Overview", font=('Inter', 18, 'bold'), foreground='#28a745', background='white').pack(anchor=tk.NW, pady=(0, 10))

        self.ticket_labels = {}
        ticket_info = [
            ("Online Tickets Sold:", "online_sold", '#28a745', False),
            ("Offline Tickets Sold:", "offline_sold", '#28a745', False),
            ("Total Tickets (Confirmed):", "total_confirmed", '#28a745', False),
            ("Waitlisted Passengers:", "waitlisted", '#e6b800', False),
            ("Total Expected Passengers:", "total_expected", '#2a6496', True) # Last one is bold
        ]

        for i, (text, key, color, bold) in enumerate(ticket_info):
            row_frame = ttk.Frame(ticket_data_frame, style='TFrame')
            row_frame.pack(fill=tk.X, pady=2)
            ttk.Label(row_frame, text=text, font=('Inter', 10, 'bold' if bold else 'normal'), background='white').pack(side=tk.LEFT, anchor=tk.W)
            value_label = ttk.Label(row_frame, text="0", font=('Inter', 14, 'bold' if bold else 'normal'), foreground=color, background='white')
            value_label.pack(side=tk.RIGHT, anchor=tk.E)
            self.ticket_labels[key] = value_label
            if bold: # Add a separator for the total line
                ttk.Separator(ticket_data_frame, orient='horizontal').pack(fill=tk.X, pady=(5, 5))


        # --- Bottom Section: Camera Feeds ---
        camera_feeds_frame = ttk.Frame(main_content_frame, style='TFrame', padding=15)
        camera_feeds_frame.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, pady=(10, 0), padx=0)
        camera_feeds_frame.grid_columnconfigure(0, weight=1) # Allow content to expand

        ttk.Label(camera_feeds_frame, text="Live Camera Feeds", font=('Inter', 18, 'bold'), foreground='#6a0dad', background='white').pack(anchor=tk.NW, pady=(0, 10))

        self.camera_widgets = []
        camera_data = [
            {'id': 'cam001', 'location': 'Main Entrance', 'crowdCount': 0, 'density': 0, 'active': True},
            {'id': 'cam002', 'location': 'Platform 1', 'crowdCount': 0, 'density': 0, 'active': True},
            {'id': 'cam003', 'location': 'Platform 2', 'crowdCount': 0, 'density': 0, 'active': True},
            {'id': 'cam004', 'location': 'Exit Gate', 'crowdCount': 0, 'density': 0, 'active': True},
        ]
        
        camera_grid_frame = ttk.Frame(camera_feeds_frame, style='TFrame')
        camera_grid_frame.pack(fill=tk.BOTH, expand=True)
        for i, cam in enumerate(camera_data):
            col = i % 4
            row = i // 4
            camera_card = ttk.Frame(camera_grid_frame, style='TFrame', padding=10, relief=tk.GROOVE, borderwidth=1)
            camera_card.grid(row=row, column=col, sticky=tk.NSEW, padx=5, pady=5)
            camera_grid_frame.grid_columnconfigure(col, weight=1)

            ttk.Label(camera_card, text=f"{cam['location']} ({cam['id']})", font=('Inter', 12, 'bold'), background='white').pack(anchor=tk.NW, pady=(0, 5))
            
            # Placeholder for video feed
            video_placeholder = tk.Canvas(camera_card, width=150, height=90, bg='#cccccc', relief=tk.SOLID, borderwidth=1)
            video_placeholder.pack(pady=(0, 5))
            video_placeholder.create_text(75, 45, text="Live Feed", fill="#666666", font=('Inter', 10))

            count_label = ttk.Label(camera_card, text=f"Crowd Count: 0", font=('Inter', 10), background='white')
            count_label.pack(anchor=tk.NW)
            density_label = ttk.Label(camera_card, text=f"Density: 0%", font=('Inter', 10), background='white')
            density_label.pack(anchor=tk.NW)
            
            self.camera_widgets.append({
                'id': cam['id'],
                'location': cam['location'],
                'count_label': count_label,
                'density_label': density_label,
                'density_value': 0 # To store the actual density value for color logic
            })

        # Initial data setup
        self.station_status = {
            'totalInflow': 0,
            'platform1Density': 0,
            'platform2Density': 0,
            'entranceDensity': 0,
            'exitDensity': 0,
        }
        self.ticket_data = {
            'online_sold': 1500,
            'offline_sold': 800,
            'waitlisted': 350,
        }
        self.alerts = []
        self.alert_id_counter = 0

        self.update_data() # Start the simulation update loop

    def get_density_color_code(self, density):
        """Returns hex color code based on density."""
        if density > 1850: 
            return '#cc0000' # Critical Red
        if density > 1600: 
            return '#e6b800' # High Yellow
        if density > 1000: 
            return '#28a745'
        return '#2a6496' # Low Blue

    def update_data(self):
        """Simulates real-time data updates and refreshes the GUI."""
        # Update Time
        self.time_label.config(text=f"Station: Central Terminal\n{time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Simulate Inflow and Density
        new_inflow = random.randint(5, 25)
        self.station_status['totalInflow'] += new_inflow

        for area in ['platform1Density', 'platform2Density', 'entranceDensity', 'exitDensity']:
            change = random.uniform(-5, 10) # Can increase or decrease
            if area == 'entranceDensity': # More fluctuation for entrance
                change = random.uniform(-7, 15)
            self.station_status[area] = max(0, min(100, self.station_status[area] + change))

        # Update Dashboard Density Labels
        self.density_labels["Entrance"].config(text=f"Entrance ({int(self.station_status['entranceDensity'])}%)", background=self.get_density_color_code(self.station_status['entranceDensity']))
        self.density_labels["Platform 1"].config(text=f"Platform 1 ({int(self.station_status['platform1Density'])}%)", background=self.get_density_color_code(self.station_status['platform1Density']))
        self.density_labels["Platform 2"].config(text=f"Platform 2 ({int(self.station_status['platform2Density'])}%)", background=self.get_density_color_code(self.station_status['platform2Density']))
        self.density_labels["Exit"].config(text=f"Exit ({int(self.station_status['exitDensity'])}%)", background=self.get_density_color_code(self.station_status['exitDensity']))

        # Update Key Metrics
        self.total_inflow_label.config(text=str(self.station_status['totalInflow']))
        self.waitlisted_held_label.config(text=str(self.ticket_data['waitlisted']))

        # Generate Alerts
        new_alerts_generated = []
        if self.station_status['platform1Density'] > 85:
            new_alerts_generated.append({'type': 'CRITICAL', 'message': f"Platform 1: Critical density ({int(self.station_status['platform1Density'])}%)! Action required."})
        elif self.station_status['platform1Density'] > 60 and self.station_status['platform1Density'] <= 65:
            new_alerts_generated.append({'type': 'WARNING', 'message': f"Platform 1: High density ({int(self.station_status['platform1Density'])}%). Monitor closely."})

        if self.station_status['platform2Density'] > 85:
            new_alerts_generated.append({'type': 'CRITICAL', 'message': f"Platform 2: Critical density ({int(self.station_status['platform2Density'])}%)! Action required."})
        elif self.station_status['platform2Density'] > 60 and self.station_status['platform2Density'] <= 65:
            new_alerts_generated.append({'type': 'WARNING', 'message': f"Platform 2: High density ({int(self.station_status['platform2Density'])}%). Monitor closely."})

        if self.station_status['entranceDensity'] > 90:
            new_alerts_generated.append({'type': 'CRITICAL', 'message': f"Main Entrance: Extreme congestion ({int(self.station_status['entranceDensity'])}%)! Consider restricting entry."})
        elif self.station_status['entranceDensity'] > 70 and self.station_status['entranceDensity'] <= 75:
            new_alerts_generated.append({'type': 'WARNING', 'message': f"Main Entrance: High inflow detected ({int(self.station_status['entranceDensity'])}%)."})

        for alert in new_alerts_generated:
            self.alert_id_counter += 1
            self.alerts.append(alert)
            self.alerts_text.insert(tk.END, f"{time.strftime('%H:%M:%S')} - {alert['message']}\n", alert['type'])
            self.alerts_text.see(tk.END) # Scroll to bottom

        # Simulate Ticket Data Changes
        self.ticket_data['online_sold'] += random.randint(0, 5)
        self.ticket_data['offline_sold'] += random.randint(0, 3)
        self.ticket_data['waitlisted'] = max(0, self.ticket_data['waitlisted'] - random.randint(0, 2))

        self.ticket_labels['online_sold'].config(text=str(self.ticket_data['online_sold']))
        self.ticket_labels['offline_sold'].config(text=str(self.ticket_data['offline_sold']))
        self.ticket_labels['total_confirmed'].config(text=str(self.ticket_data['online_sold'] + self.ticket_data['offline_sold']))
        self.ticket_labels['waitlisted'].config(text=str(self.ticket_data['waitlisted']))
        self.ticket_labels['total_expected'].config(text=str(self.ticket_data['online_sold'] + self.ticket_data['offline_sold'] + self.ticket_data['waitlisted']))

        # Simulate Camera Feed Updates
        for cam_widget in self.camera_widgets:
            # Base crowd count on density value for more realistic simulation
            new_count = cam_widget['density_value'] + random.uniform(-2, 5)
            new_count = max(0, int(new_count * 5)) # Scale density to a count (e.g., 100% density = ~500 people)
            
            new_density = max(0, min(100, cam_widget['density_value'] + random.uniform(-5, 10)))
            cam_widget['density_value'] = new_density # Update internal density value

            cam_widget['count_label'].config(text=f"Crowd Count: {new_count}")
            cam_widget['density_label'].config(text=f"Density: {int(new_density)}%", foreground=self.get_density_color_code(new_density))

        # Schedule the next update
        self.master.after(3000, self.update_data) # Update every 3 seconds

# Create the main window
root = tk.Tk()
app = RailGuardProApp(root)
root.mainloop()
