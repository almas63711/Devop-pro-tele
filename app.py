import os
import asyncio
import subprocess
import webbrowser
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ==========================================
# 🔑 CONFIGURATION AREA
# ==========================================
BOT_TOKEN = "8988049569:AAHzI8xAlcSyc3D18UEM2Vk6RdfCS8Hq7Z4"
ADMIN_ID = 8245337852 

# 👇 CONFIGURABLE ALARM URL TRACK 👇
TARGET_SONG_URL = "https://youtube.com/shorts/MOf7db2uYo4?si=AN6IDuPNj7Cf3wFc"

# 🔒 Global safety flag to prevent loop spam and network drops
is_alarm_active = False


# ==========================================
# 🔒 SECURITY ACCESS CONTROL
# ==========================================
def check_security(update: Update) -> bool:
    return update.effective_user.id == ADMIN_ID


# ==========================================
# 🚀 CORE DEVOPS INTERFACE FUNCTIONS (1 - 6)
# ==========================================

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_security(update): return
    await update.message.reply_text("⏳ Inspecting local Docker container layers...")
    result = subprocess.run(["docker", "ps", "--filter", "name=test-web-server", "--format", "table {{.Names}}\t{{.Status}}"], capture_output=True, text=True, shell=True)
    output = result.stdout.strip() if result.stdout else "No active Docker containers found on this server node."
    await update.message.reply_text(f"📋 **Host Server Node State:**\n```\n{output}\n```", parse_mode="Markdown")

async def metrics_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_security(update): return
    await update.message.reply_text("📊 Gathering hardware performance layers...")
    cmd = 'powershell "Get-Volume -DriveLetter C | Select-Object SizeRemaining, Size | Format-Table -HideTableHeaders"'
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    output = result.stdout.strip() if result.stdout else "Unable to parse local hard disk sectors."
    await update.message.reply_text(f"🖥️ **Storage Metrics (C: Drive Remaining Space):**\n```\n{output}\n```", parse_mode="Markdown")

async def deploy_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global is_alarm_active
    if not check_security(update): return
    await update.message.reply_text("🚀 Initializing live Docker deployment pipeline...")
    subprocess.run("docker rm -f test-web-server", capture_output=True, text=True, shell=True)
    cmd = "docker run -d --name test-web-server -p 8080:80 nginx"
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        is_alarm_active = False  # Reset flag on deploy
        await update.message.reply_text("✅ **Deployment Complete!**\nNginx container (`test-web-server`) is live on port 8080.", parse_mode="Markdown")
    else:
        await update.message.reply_text(f"❌ **Deployment Failed:**\n```\n{result.stderr.strip()}\n```", parse_mode="Markdown")

async def logs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_security(update): return
    if not context.args:
        await update.message.reply_text("⚠️ Specify container name. Example: `/logs test-web-server`")
        return
    container_name = " ".join(context.args)
    cmd = f"docker logs --tail 15 {container_name}"
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    log_output = result.stdout.strip() if result.stdout else result.stderr.strip()
    await update.message.reply_text(f"🪵 **Logs for `{container_name}`:**\n```\n{log_output}\n```", parse_mode="Markdown")

async def fix_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global is_alarm_active
    if not check_security(update): return
    await update.message.reply_text("🛠️ **Initiating Automated Infrastructure Self-Healing Loop...**", parse_mode="Markdown")
    
    # Safely terminate browser windows to silence the alarm
    subprocess.run("taskkill /IM chrome.exe /F", capture_output=True, text=True, shell=True)
    subprocess.run("taskkill /IM msedge.exe /F", capture_output=True, text=True, shell=True)
    
    subprocess.run("docker rm -f test-web-server", capture_output=True, text=True, shell=True)
    subprocess.run("docker system prune -f", capture_output=True, text=True, shell=True)
    cmd = "docker run -d --name test-web-server -p 8080:80 nginx"
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    
    if result.returncode == 0:
        is_alarm_active = False  # Disarm the flag state completely
        await update.message.reply_text("✅ **Self-Healing Complete!** System running clean on port 8080. Alarm audio terminated safely.")
    else:
        await update.message.reply_text(f"❌ **Self-Healing Failed:**\n```\n{result.stderr.strip()}\n```", parse_mode="Markdown")

async def open_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not check_security(update): return
    if not context.args: return
    app_choice = " ".join(context.args).lower()
    if app_choice == "explorer": os.system("start explorer C:\\")
    elif app_choice == "chrome": os.system("start chrome")
    elif app_choice == "notepad": os.system("start notepad")
    elif app_choice == "code": os.system(r'start C:\Users\maham\AppData\Local\Programs\Microsoft\"VS Code\"\Code.exe')
    elif app_choice == "whatsapp": webbrowser.open("https://whatsapp.com")
    await update.message.reply_text(f"🤖 Triggered desktop app: `{app_choice}`")


# =======================================================
# 🕵️‍♂️ PROACTIVE ALARM MONITORING ENGINE (ZERO TRACEBACK TRAP)
# =======================================================
async def background_monitoring_loop(app):
    global is_alarm_active
    print("📈 Background Monitoring Daemon Thread Initialized successfully...")
    await asyncio.sleep(5)
    
    while True:
        try:
            # Check if container signature is running smoothly inside active shell loops
            check_cmd = "docker ps --filter name=test-web-server --format {{.Names}} | findstr test-web-server"
            result = subprocess.run(check_cmd, capture_output=True, text=True, shell=True)
            
            if "test-web-server" not in result.stdout:
                # 🔒 Only trigger if the alarm isn't already active. This keeps the network polling stable.
                if not is_alarm_active:
                    print("🚨 CRITICAL METRIC REACHED: Production container is OFFLINE!")
                    is_alarm_active = True  
                    
                    # Launch your custom track url
                    webbrowser.open(TARGET_SONG_URL)
                    
                    error_msg = (
                        "🚨 **CRITICAL INFRASTRUCTURE ALERT!**\n\n"
                        "💥 **Target Node**: `test-web-server` has crashed or stopped unexpectedly!\n"
                        "🔊 **Siren Active**: Emergency alarm music is blasting on your server node.\n"
                        "🛠️ Action Recommended: Send `/fix` to stop the sound and self-heal the container immediately."
                    )
                    await app.bot.send_message(chat_id=ADMIN_ID, text=error_msg, parse_mode="Markdown")
            
        except Exception as e:
            print(f"Internal monitor error: {e}")
            
        # Frequency check timer holds loop without breaking API integrations
        await asyncio.sleep(20)


# ==========================================
# ⚡ CORE INITIALIZATION MAIN ENGINE
# ==========================================
async def main():
    print("🤖 ChatOps Automation Agent Core is initializing...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CommandHandler("metrics", metrics_command))
    app.add_handler(CommandHandler("deploy", deploy_command))
    app.add_handler(CommandHandler("logs", logs_command))
    app.add_handler(CommandHandler("fix", fix_command))
    app.add_handler(CommandHandler("open", open_command))

    await app.initialize()
    await app.start()
    
    asyncio.create_task(background_monitoring_loop(app))
    
    print("✅ Connection secure. Engine is polling for inputs and running background analytics...")
    await app.updater.start_polling()
    
    try:
        while True:
            await asyncio.sleep(3600)
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 Shutting down ChatOps engine safely...")

if __name__ == "__main__":
    asyncio.run(main())
