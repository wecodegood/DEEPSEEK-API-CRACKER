def GetLastResponse(page):
    import time
    
    # Wait for any message to appear
    page.wait_for_selector(".ds-message", timeout=10000)
    
    # Wait for response to finish generating
    last_text = ""
    stable_count = 0
    started = False
    
    while True:  # Wait indefinitely until response is complete
        try:
            messages = page.locator("xpath=//div[contains(@class, 'ds-message')]").all()
            
            if messages:
                current_text = messages[-1].text_content()
                
                # Check if response has started (at least 5 characters)
                if not started and len(current_text) >= 5:
                    started = True
                
                # Only start monitoring after response has started
                if started:
                    # If text hasn't changed for 5 checks, assume it's done
                    if current_text == last_text:
                        stable_count += 1
                        if stable_count >= 5:
                            return current_text
                    else:
                        stable_count = 0
                        last_text = current_text
        except:
            pass
        
        # time.sleep(0.2)  # Check every 0.2 seconds for faster response
