# Canva MCP Setup Guide (via Zapier)

## Step 1: Generate Your Zapier MCP Endpoint

You need to create a custom MCP endpoint that will connect Claude Code to your Canva account.

### Instructions:

1. **Visit Zapier MCP for Canva:**
   - Go to: https://zapier.com/mcp/canva

2. **Click "Generate MCP Endpoint"** (or similar button)
   - You'll need to log in to your Zapier account
   - If you don't have Zapier, you'll need to sign up (free tier available)

3. **Select Canva Actions:**
   When prompted, select these actions:
   - ✅ Create Design
   - ✅ Find Design
   - ✅ Export Design
   - ✅ Upload Asset
   - ✅ API Request (Beta) - for custom operations

4. **Connect Your Canva Account:**
   - Zapier will prompt you to authenticate with Canva
   - Log in with your Canva account credentials
   - Grant Zapier permission to access Canva

5. **Copy Your MCP Endpoint URL:**
   - You'll receive a unique URL like: `https://mcp.zapier.com/[YOUR-UNIQUE-ID]`
   - **COPY THIS URL** - we'll need it in the next step

## Step 2: Configure Claude Code MCP Settings

Once you have your Zapier MCP endpoint URL, we need to add it to Claude Code's configuration.

### Find Your Claude Code Config File:

The config file location depends on your OS:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

### Add Canva MCP Configuration:

1. Open the config file in a text editor
2. Add this configuration (replace `YOUR-ZAPIER-MCP-URL` with your actual URL):

```json
{
  "mcpServers": {
    "canva": {
      "url": "YOUR-ZAPIER-MCP-URL"
    }
  }
}
```

If you already have other MCP servers configured, add the "canva" entry to the existing "mcpServers" object:

```json
{
  "mcpServers": {
    "existing-server": {
      "command": "some-command"
    },
    "canva": {
      "url": "YOUR-ZAPIER-MCP-URL"
    }
  }
}
```

3. Save the file
4. **Restart Claude Code** for changes to take effect

## Step 3: Verify Connection

After restarting Claude Code, let me know and I'll test the Canva MCP connection by attempting to:
1. List available Canva tools
2. Create a simple test design
3. Export it

## What You Need to Do NOW:

1. Go to https://zapier.com/mcp/canva
2. Generate your MCP endpoint
3. Copy the URL they give you
4. Share the URL with me (or just confirm you have it)

Then I'll help you configure Claude Code and test the connection.

## Important Notes:

- **Task Usage:** Each MCP call uses 2 tasks from your Zapier plan quota
- **Authentication:** Handled automatically through the MCP URL
- **Security:** The URL is private and includes authentication tokens
- **Zapier Plan:** Free tier should work for testing, but may need paid plan for bulk operations

---

**Ready?** Go ahead and generate your Zapier MCP endpoint, then let me know when you have the URL!
